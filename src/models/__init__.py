from ..extensions import login_manager
from .users import User


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)
