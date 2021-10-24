from .app import socketio
from flask import request
from flask_socketio import emit, join_room, leave_room

#   using this until I get around to using redis
active_users = {'1': set(), '2': set(), '3': set()}


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
    active_users[room].add(username)
    users = list(active_users[room])
    join_room(room)
    emit('active_users_update', {'active_users': users}, to=room)


@socketio.on('leave_room_request')
def handle_leave_room_request(data):
    username = data['username']
    room = data['room_id']
    active_users[room].remove(username)
    users = list(active_users[room])
    emit('active_users_update', {'active_users': users}, to=room)
    leave_room(room)


@socketio.on('active_users_request')
def handle_active_users_request(data):
    room = data['room_id']
    users = list(active_users[room])
    emit('active_users_update', {'active_users': users})


@socketio.on('message')
def handle_message(data):
    room = data['room_id']
    emit('message', data, to=room)


#   notifications aren't used right now by the client
#   but might be later on by admins or for broadcasts
@socketio.on('notification')
def handle_notification(data):
    room = data['room_id']
    emit('notification', data, to=room)