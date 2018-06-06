import re, os

from flask import Blueprint, jsonify, request, session, render_template
from sqlalchemy import or_

from utils import status_code
from utils.settings import UPLOAD_DIRS
from utils.functions import check_login
from .models import User

# 用户模块蓝图
user_blue = Blueprint('user', __name__)


"""---------------------------------页面跳转---------------------------------"""


@user_blue.route('/login/', methods=['GET'])
def login_page():

    return render_template('login.html')


@user_blue.route('/inspecte/', methods=['GET'])
@check_login
def inspecte_page():

    return render_template('inspecte.html')


@user_blue.route('/inspectoradd/', methods=['GET'])
@check_login
def inspector_add_page():

    return render_template('inspector_add.html')


@user_blue.route('/manage/', methods=['GET'])
@check_login
def inspector_manage_page():
    return render_template('inspector_manage.html')


@user_blue.route('/inspectormodify/', methods=['GET'])
@check_login
def inspector_modify_page():
    return render_template('inspector_modify.html')


# @user_blue.route('/inspectorsearch/', methods=['GET'])
# @check_login
# def inspector_search_page():
#     return render_template('inspector_search.html')


"""---------------------------------接口功能---------------------------------"""


# 登录接口
@user_blue.route('/login/', methods=['POST'])
def login():

    info_dict = request.form

    username = info_dict['username']
    passwd = info_dict['password']

    user = User.query.filter(User.username == username).first()

    if not user:  # 没有这个用户
        return jsonify(status_code.USER_IS_NOT_EXISTS)

    if user.user_type == 0:
        if user.check_pwd(passwd):  # 检验密码
            session['user_id'] = user.id
            return jsonify(code=status_code.SUCCESS['code'], user_info=user.to_dict())
        else:
            return jsonify(status_code.USER_PASSWORD_ERROR)
    else:
        if user.passwd_hash == passwd:
            session['user_id'] = user.id
            return jsonify(code=status_code.SUCCESS['code'], user_info=user.to_dict())
        else:
            return jsonify(status_code.USER_PASSWORD_ERROR)


# 获取登录用户信息接口
@user_blue.route('/userinfo/', methods=['GET'])
def user_info():

    if 'user_id' not in session:
        return jsonify(status_code.USER_NOT_LOGIN)

    user = User.query.get(session['user_id'])

    return jsonify(code=status_code.SUCCESS['code'], user_info=user.to_dict())


# 退出登录接口
@user_blue.route('/logout/', methods=['GET'])
def logout():

    session.clear()

    return render_template('index.html')


# 管理员更改密码接口
@user_blue.route('/changepassword/', methods=['POST'])
@check_login
def change_passwd():

    user_id = session['user_id']

    user = User.query.get(user_id)

    if not user:  # 用户名不存在
        return jsonify(status_code.USER_IS_NOT_EXISTS)

    old_passwd = request.form['old_password']
    if not user.check_pwd(old_passwd):  # 密码不正确
        return jsonify(status_code.USER_PASSWORD_ERROR)

    user.password = request.form['new_password']

    try:
        user.add_update()
        session.clear()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 上传头像接口
@user_blue.route('/upload/', methods=['POST'])
@check_login
def upload():

    user_id = session['user_id']
    user = User.query.get(user_id)

    if not user:
        return jsonify(status_code.USER_IS_NOT_EXISTS)

    avatar = request.files['avatar']

    if not re.match(r'^image/.*$', avatar.mimetype):  # 判断是否是图像格式
        return jsonify(status_code.PARAMS_ERROR)

    file_url = os.path.join(UPLOAD_DIRS, user_id)
    save_url = os.path.join(file_url, avatar.filename)

    if not os.path.exists(file_url):
        os.makedirs(file_url)

    avatar.save(save_url)

    user.avatar = os.path.join('/static/upload/%s' % user_id, avatar.filename)

    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 搜索质检员接口
@user_blue.route('/inspector/', methods=['POST'])
@check_login
def show_inspector():

    user_id = session['user_id']

    user = User.query.get(user_id)
    if user.user_type != 0:
        return jsonify(status_code.USER_NOT_MANAGER)

    info_dict = request.form

    inspector_info = info_dict.get('search_info', '')

    users = User.query.filter(User.user_type == 1)

    if inspector_info:  # 通过模糊查找找到质检员
        users = users.filter(or_(User.id==inspector_info, User.name.like('%' + inspector_info + '%'))).all()
        if not users:
            return jsonify(status_code.SEARCH_RESULT_IS_NULL)

    inspector_list = []
    for user in users:
        inspector_list.append(user.to_inspector_dict())

    return jsonify(code=status_code.SUCCESS['code'], inspector_list=inspector_list)


# 增加质检员接口
@user_blue.route('/addinspector/', methods=['POST'])
@check_login
def add_inspector():
    user_id = session['user_id']

    user = User.query.get(user_id)
    if user.user_type != 0:
        return jsonify(status_code.USER_NOT_MANAGER)

    info_dict = request.form

    username = info_dict['username']
    name = info_dict['name']
    password = info_dict['password']
    inspector_id = info_dict['inspector_id']

    if not all((username, name, password)):
        return jsonify(status_code.PARAMS_ERROR)

    new_user = User()
    if inspector_id:
        if User.query.get(inspector_id):  # 如果用户编号已存在
            return jsonify(status_code.USER_IS_ALREADY_EXISTS)
        new_user.id = inspector_id
    new_user.username = username
    new_user.name = name
    new_user.passwd_hash = password
    new_user.user_type = 1

    try:
        new_user.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 修改质检员接口
@user_blue.route('/changeinspector/', methods=['POST'])
@check_login
def change_inspector():
    user_id = session['user_id']

    user = User.query.get(user_id)
    if user.user_type != 0:
        return jsonify(status_code.USER_NOT_MANAGER)

    info_dict = request.form

    username = info_dict['username']
    name = info_dict['name']
    password = info_dict['password']
    inspector_id = info_dict['inspector_id']

    if not all((username, name, password)):
        return jsonify(status_code.PARAMS_ERROR)

    change_user = User.query.get(inspector_id)
    if not change_user:
        return jsonify(status_code.USER_IS_NOT_EXISTS)
    if change_user.user_type == 0:
        return jsonify(status_code.USER_CAN_NOT_CHANGE_MANAGER)
    change_user.username = username
    change_user.name = name
    change_user.passwd_hash = password

    try:
        change_user.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# 删除质检员接口
@user_blue.route('/delinspector/', methods=['POST'])
@check_login
def del_inspector():

    user_id = session['user_id']

    user = User.query.get(user_id)
    if user.user_type != 0:
        return jsonify(status_code.USER_NOT_MANAGER)

    info_dict = request.form
    del_id = info_dict['inspector_id']

    del_user = User.query.get(del_id)

    if not del_user:
        return jsonify(status_code.USER_IS_NOT_EXISTS)

    if del_user.user_type == 0:
        return jsonify(status_code.USER_CAN_NOT_DEL_MANAGER)

    try:
        del_user.delete()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


# # 创建表接口
# @user_blue.route('/createtable/')
# def create_table():
#
#     db.create_all()
#
#     return '创建成功'
#
# # 创建管理员接口
# @user_blue.route('/createmanager/')
# def create_manager():
#
#     user = User()
#
#     user.username = 'admin'
#     user.password = '123456'
#     user.name = '管理员1号'
#     user.user_type = 0
#
#     try:
#         user.add_update()
#         return '创建成功'
#     except:
#         return '创建失败'
