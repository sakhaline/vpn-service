from ..models.users import User
from .base_repo import BaseRepository


class UserRepository(BaseRepository):
    model = User

    def create_user(self, data: dict):
        self.create(data)

    def get_user_by_id(self, user_id):
        return self.get_by_id(user_id)

    def get_user_list(self):
        return self.get_list()

    def update_user(self, user: int, data: dict):
        user.username = data["username"]
        user.email = data["email"]
        self.db.session.commit()
        return user

    def delete_user(self, user_id):
        self.delete(user_id)

    def get_user_by_username(self, username):
        return self.db.session.execute(
            self.db.select(self.model).where(self.model.username == username)
        ).scalar()
