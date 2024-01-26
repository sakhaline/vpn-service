class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_user(self, data):
        return self.user_repo.create_user(data)

    def get_user_by_id(self, user_id):
        return self.user_repo.get_user_by_id(user_id)

    def get_user_list(self):
        return self.user_repo.get_user_list()

    def update_user(self, user_id, data):
        return self.user_repo.update_user(user_id, data)

    def delete_user(self, user_id):
        return self.user_repo.delete_user(user_id)
