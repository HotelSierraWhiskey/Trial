from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_cors import CORS
from .user import User


app = Flask(__name__)

app.config.update(config)

db = SQLAlchemy(app)

login_manager = LoginManager(app)

socketio = SocketIO(app)

CORS(app)

@login_manager.user_loader
def load_user(user_id):
    query = db.session.execute(f"SELECT username FROM trial.users WHERE id='{user_id}'")
    username = query.first()[0]
    user = User(username, user_id)
    return user