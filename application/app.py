from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_cors import CORS


app = Flask(__name__)

app.config.update(config)

db = SQLAlchemy(app)

login_manager = LoginManager(app)

socketio = SocketIO(app)

CORS(app)