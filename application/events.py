from .app import socketio, app
from flask import request
from flask_socketio import emit, join_room, leave_room, rooms
from .general_utils import get_room_name_from_id
from .admin_utils import create_room, delete_room, add_active_user_to, remove_active_user_from, get_active_users_from


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
    add_active_user_to(room, username)
    users = get_active_users_from(room)
    join_room(room)
    emit('active_users_update', {'active_users': users}, to=room)


@socketio.on('leave_room_request')
def handle_leave_room_request(data):
    username = data['username']
    room = data['room_id']
    remove_active_user_from(room, username)
    users = get_active_users_from(room)
    emit('active_users_update', {'active_users': users}, to=room)
    leave_room(room)


@socketio.on('room_name_request')
def handle_room_name_request(data):
    room_id = data['room_id']
    room_name = get_room_name_from_id(room_id)
    if room_name:
        emit('room_name_update', {'room_name': room_name})
    else:
        print('Error')


@socketio.on('active_users_request')
def handle_active_users_request(data):
    room = data['room_id']
    users = get_active_users_from(room)
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


@socketio.on('create_room')
def handle_create_room(data):
    name = data['name']
    create_room(name)


@socketio.on('delete_room')
def handle_delete_room(data):
    name = data['name']
    delete_room(name)
