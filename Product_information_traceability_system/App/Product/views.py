import re, os

from flask import Blueprint, jsonify, session, request, render_template
from sqlalchemy import or_

from utils import status_code
from .models import Product, Batch
from App.User.models import User
from utils.functions import check_login
from utils.settings import GOODS_DIRS

product_blue = Blueprint('product', __name__)
index_blue = Blueprint('index', __name__)


"""---------------------------------页面跳转---------------------------------"""


@index_blue.route('/', methods=['GET'])
def index():
    """主页"""
    return render_template('index.html')


@product_blue.route('/manage/', methods=['GET'])
@check_login
def product_manage_page():
    """管理商品"""
    return render_template('product_manage.html')


@product_blue.route('/productsearch/', methods=['GET'])
def product_search_page():
    """查询产品"""
    return render_template('product_search.html')


@product_blue.route('/productmodify/', methods=['GET'])
@check_login
def product_modify_page():
    """修改产品信息"""
    return render_template('product_modify.html')


@product_blue.route('/productadd/', methods=['GET'])
@check_login
def product_add_page():
    """增加产品"""
    return render_template('product_add.html')


@product_blue.route('/productinfo/', methods=['GET'])
def product_info_page():
    """产品详情"""
    return render_template('product_info.html')


@product_blue.route('/productmsearch/', methods=['GET'])
@check_login
def product_manager_search_page():
    """管理员查询产品界面"""
    return render_template('product_modify.html')


@product_blue.route('/submit/', methods=['GET'])
@check_login
def submit_page():
    """提交质检结果"""
    return render_template('inspecte.html')


"""---------------------------------接口功能---------------------------------"""


# 主页案例展示接口
@product_blue.route('/index/', methods=['GET'])
def index():

    products = Product.query.order_by(Product.update_time).limit(4)

    product_list = []
    for product in products:
        product_list.append(product.to_dict())

    return jsonify(code=status_code.SUCCESS['code'], product_list=product_list)


# 获取产品详情接口
@product_blue.route('/productinfo/', methods=['POST'])
def product_info():
    """产品详情"""

    search_user = ''  # 默认进行搜索的是顾客

    if 'user_id'in session:

        user_id = session['user_id']
        user = User.query.get(user_id)
        search_user = user.to_dict()  # 在登录状态获取登录者的身份

    if 'product_id' not in request.form:
        return jsonify(status_code.SEARCH_RESULT_IS_NULL)
    product_id = request.form.get('product_id')
    product = Product.query.get(product_id)

    if not product:
        return jsonify(status_code.SEARCH_RESULT_IS_NULL)

    return jsonify(code=status_code.SUCCESS['code'], product=product.to_dict(), user_info=search_user)


# 搜索产品接口
@product_blue.route('/product/', methods=['POST'])
def show_product():

    products = Product.query
    if 'product_info' not in request.form:
        product_info = ''
    else:
        product_info = request.form['product_info']

    search_user = ''  # 默认进行搜索的是顾客

    if 'user_id' not in session:  # 未登录，顾客浏览状态

        if not product_info:  # 没有输入搜索字段
            products = products.all()
        else:
            products = filter_product(products, product_info)

    else:
        user_id = session['user_id']
        user = User.query.get(user_id)
        search_user = user.to_dict()  # 在登录状态获取登录者的身份
        if user.user_type == 0:  # 管理员

            if not product_info:  # 没有输入搜索字段
                products = products.all()
            else:
                products = filter_product(products, product_info)
        else:
            products = products.filter(Product.inspector_id == user.id)
            products = filter_product(products, product_info)

    if not products:
        return jsonify(status_code.SEARCH_RESULT_IS_NULL)

    product_list = []
    for product in products:
        product_list.append(product.to_dict())

    return jsonify(code =status_code.SUCCESS['code'], product_list=product_list, user_info=search_user)


# 模糊搜索商品，返回结果
def filter_product(products, product_info):
    product_list = products.filter(or_(
        Product.id == product_info,
        Product.name.like('%' + product_info + '%'),
        Product.desc.like('%' + product_info + '%'),
        Product.batch_id == product_info)).all()

    return product_list


# 修改产品信息接口
@product_blue.route('/changeproduct/', methods=['POST'])
@check_login
def change_product():
    user_id = session['user_id']

    user = User.query.get(user_id)
    if user.user_type != 0:
        return jsonify(status_code.USER_NOT_MANAGER)

    info_dict = request.form
    file_dict = request.files

    batch_id = info_dict['batch_id']
    name = info_dict['name']
    desc = info_dict['desc']
    product_id = info_dict['product_id']
    inspector_id = info_dict['inspector_id']

    if not all((batch_id, name, desc, product_id, inspector_id)):
        return jsonify(status_code.PARAMS_ERROR)

    change_produ = Product.query.get(product_id)

    batch = Batch.query.get(batch_id)
    if not batch:
        batch = Batch()
        batch.id = batch_id
        try:
            batch.add_update()
        except:
            return jsonify(status_code.DATABASE_ERROR)

    if int(inspector_id) == int(user_id):
        return jsonify(status_code.PRODUCT_NOT_GET_MANAGER)

    if not User.query.get(inspector_id):
        return jsonify(status_code.USER_IS_NOT_EXISTS)

    if not change_produ:
        return jsonify(status_code.PRODUCT_IS_NOT_EXISTS)
    change_produ.name = name
    change_produ.desc = desc
    change_produ.batch_id = batch_id
    change_produ.inspector_id = inspector_id
    # change_produ = upload_good_image(file_dict, change_produ)
    upload_good_image(file_dict, change_produ)

    try:
        change_produ.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 添加产品接口
@product_blue.route('/addproduct/', methods=['POST'])
@check_login
def add_product():
    user_id = session['user_id']

    user = User.query.get(user_id)
    if user.user_type != 0:
        return jsonify(status_code.USER_NOT_MANAGER)

    info_dict = request.form
    file_dict = request.files

    batch_id = info_dict['batch_id']
    name = info_dict['name']
    desc = info_dict['desc']
    product_id = info_dict['product_id']
    inspector_id = info_dict['inspector_id']

    if not all((batch_id, name, desc, product_id, inspector_id)):
        return jsonify(status_code.PARAMS_ERROR)

    new_produ = Product()

    batch = Batch.query.get(batch_id)
    if not batch:
        batch = Batch()
        batch.id = batch_id
        try:
            batch.add_update()
        except:
            return jsonify(status_code.DATABASE_ERROR)

    if int(inspector_id) == int(user_id):
        return jsonify(status_code.PRODUCT_NOT_GET_MANAGER)

    if not User.query.get(inspector_id):
        return jsonify(status_code.USER_IS_NOT_EXISTS)

    if product_id:
        if Product.query.get(product_id):  # 如果产品编号已存在
            return jsonify(status_code.PRODUCT_IS_EXISTS)
        new_produ.id = product_id
    new_produ.desc = desc
    new_produ.name = name
    new_produ.batch_id = batch_id
    new_produ.inspector_id = inspector_id
    new_produ.status = 0
    # new_produ = upload_good_image(file_dict, new_produ)
    upload_good_image(file_dict, new_produ)

    try:
        new_produ.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 删除产品接口
@product_blue.route('/delproduct/', methods=['POST'])
@check_login
def del_product():

    user_id = session['user_id']

    user = User.query.get(user_id)
    if user.user_type != 0:
        return jsonify(status_code.USER_NOT_MANAGER)

    info_dict = request.form
    del_id = info_dict['product_id']

    del_produ = Product.query.get(del_id)

    if not del_produ:
        return jsonify(status_code.PRODUCT_IS_NOT_EXISTS)

    try:
        del_produ.delete()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 提交质检结果接口
@product_blue.route('/submit/', methods=['POST'])
@check_login
def submit_result():
    user_id = session['user_id']

    info_dict = request.form
    product_id = info_dict['product_id']
    status = info_dict['status']

    produ = Product.query.get(product_id)
    if not produ:
        return jsonify(status_code.PRODUCT_IS_NOT_EXISTS)

    if produ.inspector_id != user_id:
        return jsonify(status_code.PRODUCT_NOT_YOURS)

    if produ.status != 0:
        return jsonify(status_code.PRODUCT_ALREADY_CHANGED)

    produ.status = status

    try:
        produ.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 上传图片
def upload_good_image(file_dict, product):

    image = file_dict['product_image']

    if not re.match(r'^image/.*$', image.mimetype):  # 判断是否是图像格式
        return jsonify(status_code.PARAMS_ERROR)

    file_url = os.path.join(GOODS_DIRS, str(product.id))
    save_url = os.path.join(file_url, image.filename)

    if not os.path.exists(file_url):
        os.makedirs(file_url)

    image.save(save_url)

    product.image = os.path.join('/static/goods/%s' % product.id, image.filename)

    return product


# 产品批次接口
@product_blue.route('/batch/', methods=['GET'])
def get_batch():

    batchs = Batch.query.all()
    batch_list = []
    for batch in batchs:
        batch_list.append(batch.to_dict())

    return jsonify(code=status_code.SUCCESS['code'], s=batch_list)
