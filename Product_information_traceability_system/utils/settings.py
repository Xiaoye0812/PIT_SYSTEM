import os

from .functions import create_database_config
# 项目基础相对路径
BASE_DIRS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 静态文件夹路径
STATIC_DIRS = os.path.join(BASE_DIRS, 'static')
# 网页模板文件夹路径
TEMPLATE_DIRS = os.path.join(BASE_DIRS, 'templates')
# 用户上传头像文件夹路径
UPLOAD_DIRS = os.path.join(STATIC_DIRS, 'upload')
# 商品图片文件夹路径
GOODS_DIRS = os.path.join(STATIC_DIRS, 'goods')


DATABASE_CONFIG = {
    'database': 'mysql',  # 数据库
    'driver': 'pymysql',  # 驱动
    'user': 'root',  # 用户名
    'password': '940812',  # 密码
    'host': '127.0.0.1',  # 域名
    'port': '3306',  # 端口
    'name': 'db_PIT_SYS'  # 数据库名称
}


SQLALCHEMY_DATABASE_URI = create_database_config(DATABASE_CONFIG)
