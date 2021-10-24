from .app import socketio
from flask import request
from flask_socketio import emit, join_room, leave_room

#   using this until I get around to using redis
active_users = {'1': [], '2': [], '3': []}


@socketio.on('client_connection')
def handle_connection():
    print('connect')


@socketio.on('client_disconnection')
def handle_disconnection():
    print('disconnect')


@socketio.on('join_room_request')
def handle_join_room_request(data):
    username = data['username']
    room = data['room_id']
    join_room(room)
    active_users[room].append(username)
    emit('notification', {'type': 'join', 'username': username, 'room': room})



@socketio.on('leave_room_request')
def handle_leave_room_request(data):
    username = data['username']
    room = data['room_id']
    leave_room(room)
    idx = active_users[room].index(username)
    active_users[room].pop(idx)
    emit('notification', {'type': 'leave', 'username': username, 'room': room})



@socketio.on('active_users_request')
def handle_active_users_request(data):
    room = data['room_id']
    users = active_users[room]
    emit('active_users_response', {'active_users': users})


@socketio.on('message')
def handle_message(data):
    room = data['room_id']
    emit('message', data, to=room)


@socketio.on('notification')
def handle_notification(data):
    room = data['room_id']
    emit('notification', data, to=room)