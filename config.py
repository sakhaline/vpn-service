import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLASK_APP = os.environ.get("FLASK_APP")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = "development"
