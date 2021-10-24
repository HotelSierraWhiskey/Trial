from .app import socketio
from flask import request
from flask_socketio import emit, join_room, leave_room



@socketio.on('client_connection')
def handle_connection():
    print('connect')


@socketio.on('client_disconnection')
def handle_disconnection():
    print('disconnect')


@socketio.on('join_room_request')
def handle_join_room_request(data):
    username = data['username']
    room_id = data['room_id']
    join_room(room_id)
    emit('notification', {'data': f"{username} joined room '{room_id}'"})


@socketio.on('message')
def handle_message(data):
    room = data['room_id']
    emit('message', data, to=room)


@socketio.on('notification')
def handle_notification(data):
    room = data['room_id']
    emit('notification', data, to=room)