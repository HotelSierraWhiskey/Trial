from flask_login import login_manager
from .app import db
from ..models import User


@login_manager.user_loader
def load_user(user_id):
    query = db.session.execute(f"SELECT username FROM trial.users WHERE id='{user_id}'")
    username = query.first()[0]
    user = User(username, user_id)
    return user