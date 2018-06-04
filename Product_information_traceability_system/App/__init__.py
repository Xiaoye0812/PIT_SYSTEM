
from flask import Flask

from utils.settings import STATIC_DIRS, SQLALCHEMY_DATABASE_URI, TEMPLATE_DIRS
from utils.functions import init_ext
from App.User.views import user_blue
from App.Product.views import product_blue, index_blue


def create_flask_app():

    app = Flask(__name__, static_folder=STATIC_DIRS, template_folder=TEMPLATE_DIRS)

    app.register_blueprint(blueprint=user_blue, url_prefix='/user')
    app.register_blueprint(blueprint=product_blue, url_prefix='/product')
    app.register_blueprint(blueprint=index_blue, url_prefix='')

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = 'cecret_key'

    init_ext(app)

    return app
