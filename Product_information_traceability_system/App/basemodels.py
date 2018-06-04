from datetime import datetime

from utils.functions import db


class BaseModel(object):

    # 定义基础的模型
    create_time = db.Column(db.DATETIME, default=datetime.now())
    update_time = db.Column(db.DATETIME, default=datetime.now(), onupdate=datetime.now())

    # 更新到数据库
    def add_update(self):

        db.session.add(self)
        db.session.commit()

    # 删除
    def delete(self):
        db.session.delete(self)
        db.session.commit()
