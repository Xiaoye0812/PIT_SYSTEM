
from flask_script import Manager

from App import create_flask_app

app = create_flask_app()
manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
