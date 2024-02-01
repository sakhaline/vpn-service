from flask import abort
from flask_login import logout_user, login_user
from sqlalchemy.exc import IntegrityError

from ..extensions import bcrypt


class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_user(self, data):
        try:
            data["password"] = self.hash_user_password(data["password"])
            return self.user_repo.create_user({"password": data["password"],
                                               "email": data["email"],
                                               "username": data["username"]})
        except IntegrityError:
            abort(400, 'User already exists')

    def get_user_by_id(self, user_id):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            abort(404, description="Not found")
        return user

    def get_user_list(self):
        return self.user_repo.get_user_list()

    def update_user(self, user, data):
        try:
            return self.user_repo.update_user(user, data)
        except IntegrityError:
            abort(400, 'User already exists')

    def hash_user_password(self, password):
        return bcrypt.generate_password_hash(password)

    def login(self, login_data):
        user = self.user_repo.get_user_by_username(login_data["username"])
        if not user:
            abort(401, description="Invalid username or password")

        if bcrypt.check_password_hash(user.password, login_data["password"]):
            login_user(user, remember=True)
        else:
            abort(401, description="Invalid username or password")

    def logout(self):
        logout_user()
