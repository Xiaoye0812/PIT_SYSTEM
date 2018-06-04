from werkzeug.security import generate_password_hash, check_password_hash

from App.basemodels import BaseModel, db
from App.Product.models import Product


class User(BaseModel, db.Model):

    # 用户表

    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True)  # 员工编号
    passwd_hash = db.Column(db.String(200))  # 密码
    username = db.Column(db.String(30), unique=True)  # 用户名
    name = db.Column(db.String(30))  # 姓名
    avatar = db.Column(db.String(100))  # 头像
    user_type = db.Column(db.Integer)  # 员工类型 0为管理员 1为质检员
    products = db.relationship('Product', backref='user')  # 产品

    # 读
    @property
    def password(self):
        return ''

    # 写
    @password.setter
    def password(self, pwd):
        self.passwd_hash = generate_password_hash(pwd)

    # 对比匹配
    def check_pwd(self, pwd):
        return check_password_hash(self.passwd_hash, pwd)

    def to_dict(self):
        return {
            'id': self.id,
            'avatar': self.avatar if self.avatar else '',
            'name': self.name,
            'type': self.user_type
        }

    def to_inspector_dict(self):
        return {
            'id': self.id,
            'avatar': self.avatar if self.avatar else '',
            'name': self.name,
            'username': self.username,
            'password': self.passwd_hash if self.user_type == 1 else '',
            'type': self.user_type
        }


