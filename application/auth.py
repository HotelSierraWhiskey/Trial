from flask_login import login_manager, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .app import db
from .user import User


def get_from_db(attribute, name):
    query = db.session.execute(f"SELECT {attribute} FROM trial.users WHERE username='{name}'")
    query = query.first()
    if query:
        return query[0]
    return None
    
    
def get_valid_user(form, db):
    form_name = form['login_username']
    form_password = form['login_password']

    saved_name = get_from_db('username', form_name)
    saved_hash = get_from_db('password', form_name)
    saved_id = get_from_db('id', form_name)

    if not saved_name or not saved_hash:
        return None

    if check_password_hash(saved_hash, form_password):
        return User(saved_name, saved_id)
    return None

def valid_registration(form, db):
    pass


def register_user():
    pass