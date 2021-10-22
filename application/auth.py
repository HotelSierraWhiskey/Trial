from flask_login import login_manager, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .user import User


def get_from_db(attribute, name):
    from .app import db
    query = db.session.execute(f"SELECT {attribute} FROM trial.users WHERE username='{name}'")
    query = query.first()
    if query:
        return query[0]
    return None
    
    
def get_valid_user(form):
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


def get_valid_registration(form):
    form_name = form['register_username']
    form_password = form['register_password']
    form_retype_password = form['register_repeat_password']

    if get_from_db('username', form_name):
        return None

    passwords_match = form_password == form_retype_password
    password_length_ok = len(form_password) >= 8

    print("ok")

    if passwords_match and password_length_ok:
        return {'username': form_name, 'password': form_password}


def register_user(registration):
    from .app import db
    username = registration['username']
    password_hash = generate_password_hash(registration['password'])
    db.session.execute(f"INSERT INTO trial.users(username, password) VALUES('{username}', '{password_hash}')")
    db.session.commit()