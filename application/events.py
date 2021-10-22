from .app import socketio
from flask_socketio import emit



@socketio.on('client_connection')
def connection():
    print('connect')


@socketio.on('client_disconnection')
def disconnection():
    print('disconnect')


@socketio.on('message')
def message_received(data):
    print('message')