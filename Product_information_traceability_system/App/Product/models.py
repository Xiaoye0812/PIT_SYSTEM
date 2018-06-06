
from App.basemodels import BaseModel, db, datetime


class Product(BaseModel, db.Model):

    # 产品表
    __tablename__ = 'tb_product'

    id = db.Column(db.Integer, primary_key=True)  # 产品id
    name = db.Column(db.String(100))  # 产品名称
    batch_id = db.Column(db.Integer, db.ForeignKey('tb_batch.id'), nullable=False)  # 产品批次，关联批次表
    desc = db.Column(db.String(512), nullable=True)  # 产品描述
    status = db.Column(db.Integer)  # 产品状态 0为未检测 1为通过 2为不通过
    detection_date = db.Column(db.DATETIME, default=datetime.now(), onupdate=datetime.now())  # 检测时间
    inspector_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))  # 质检员
    image = db.Column(db.String(256), default='')  # 图片

    def to_dict(self):

        return {
            'id': self.id,
            'name': self.name,
            'batch': self.batch_id,
            'desc': self.desc,
            'status': self.status,
            'detection_time': self.detection_date,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'inspector': self.user.name if self.user else '未分配',
            'image': self.image
        }


class Batch(BaseModel, db.Model):

    # 产品批次表
    __tablename__ = 'tb_batch'

    id = db.Column(db.Integer, primary_key=True)  # 批次编号
    products = db.relationship('Product', backref='batch')  # 产品

    def to_dict(self):

        return {
            'batch_id': self.id,
            'create_time': self.create_time,
            'update_time': self.update_time
        }
