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

    def update_user(self, user_id, data):
        return self.update(user_id, data)

    def delete_user(self, user_id):
        self.delete(user_id)
