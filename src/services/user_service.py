from flask import abort
from flask_login import login_user, logout_user
from sqlalchemy.exc import IntegrityError
import binascii

from ..extensions import bcrypt


class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_user(self, data):
        try:
            hashed_password = bcrypt.generate_password_hash(data["password"])
            return self.user_repo.create_user(
                {
                    "password": hashed_password,
                    "email": data["email"],
                    "username": data["username"],
                }
            )
        except IntegrityError:
            abort(400, "User already exists")

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
            abort(400, "User already exists")

    def login(self, login_data):
        user = self.user_repo.get_user_by_username(login_data["username"])
        if not user:
            abort(401, description="Invalid username")

        bytes_password_hash_from_db = binascii.unhexlify(user.password[2:])
        if bcrypt.check_password_hash(bytes_password_hash_from_db,
                                      login_data["password"]):
            login_user(user, remember=True)
        else:
            abort(401, description="Invalid password")

    def logout(self):
        logout_user()
