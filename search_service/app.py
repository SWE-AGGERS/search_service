import datetime

from flask import Flask

from search_service.views import blueprints


def create_app(debug=False):
    app = Flask(__name__)
    app.config['WTF_CSRF_SECRET_KEY'] = 'A SECRET KEY'
    app.config['SECRET_KEY'] = 'ANOTHER ONE'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # DEBUGGING AND TESTING
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['TESTING'] = debug
    app.config['LOGIN_DISABLED'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app


    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
