from flask import Flask

from config import Config

from .extensions import bcrypt, db, login_manager, migrate
from .models import User
from .routers import account, main, profile, vpn


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(main.main)
    app.register_blueprint(account.account)
    app.register_blueprint(vpn.vpn)
    app.register_blueprint(profile.profile)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.execute(db.select(User).where(User.id == user_id)).scalar()

    return app
