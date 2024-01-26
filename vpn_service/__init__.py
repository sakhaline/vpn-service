import os
from dotenv import load_dotenv

from flask import Flask

from .extensions import db, migrate, login_manager
from .routers.account import account
from .routers.vpn import vpn


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] =\
        os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =\
        os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config["FLASK_ENV"] = os.environ.get("FLASK_ENV")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(account)
    app.register_blueprint(vpn)

    return app
