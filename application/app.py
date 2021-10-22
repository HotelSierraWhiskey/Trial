from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_cors import CORS
from .user import User
from .auth import get_from_db


app = Flask(__name__)

app.config.update(config)

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

socketio = SocketIO(app)

CORS(app)


@login_manager.user_loader
def load_user(user_id):
    username = get_from_db('username', user_id)
    user = User(username, user_id)
    return user


