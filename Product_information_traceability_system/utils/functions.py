import functools

from flask import session, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from utils import status_code


db = SQLAlchemy()


def init_ext(app):

    db.init_app(app)


def create_database_config(config_dict):

    database = config_dict['database']  # 数据库
    driver = config_dict['driver']  # 驱动
    user = config_dict['user']  # 用户名
    password = config_dict['password']  # 密码
    host = config_dict['host']  # 域名
    port = config_dict['port']  # 端口
    name = config_dict['name']  # 数据库名称

    return '{}+{}://{}:{}@{}:{}/{}'.format(database, driver, user, password, host, port, name)


def check_login(func):

    @functools.wraps(func)
    def decoretor(*args, **kwargs):
        try:
            if 'user_id' in session:
                return func(*args, **kwargs)
            else:
                return redirect('/user/login/')
        except Exception as e:
            return redirect('/user/login/')

    return decoretor
