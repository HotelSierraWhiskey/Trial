import json

#   relative path from wsgi.py
rooms_json_filename = './rooms.json'



def create_room(name):
    id = name.replace(' ', '')
    room = {'name': name, 'id': id, 'href': f'rooms/{id}', 'active_users': list()}
    with open(rooms_json_filename, 'r+') as file:
        data = json.load(file)
        data['rooms'].append(room)
        file.seek(0)
        json.dump(data, file, indent=4)


def delete_room(room_id):
    with open(rooms_json_filename, 'r') as file:
        data = json.load(file)
        rooms = data['rooms']
        for i in range(len(rooms)):
            if rooms[i]['id'] == room_id:
                del data['rooms'][i]

    with open(rooms_json_filename, 'w') as file:
        json.dump(data, file, indent=4)


def get_rooms():
    with open(rooms_json_filename, 'r') as file:
        data = json.load(file)
        return data['rooms']


def add_active_user_to(room_id, username):
    with open(rooms_json_filename, 'r+') as file:
        data = json.load(file)
        rooms = data['rooms']
        for i in range(len(rooms)):
            if rooms[i]['id'] == room_id:
                if username in rooms[i]['active_users']:
                    return
                data['rooms'][i]['active_users'].append(username)

        file.seek(0)
        json.dump(data, file, indent=4)


def remove_active_user_from(room_id, username):
    with open(rooms_json_filename, 'r+') as file:
        data = json.load(file)
        rooms = data['rooms']
        for i in range(len(rooms)):
            if rooms[i]['id'] == room_id:
                if username not in rooms[i]['active_users']:
                    return
                data['rooms'][i]['active_users'].remove(username)

    with open(rooms_json_filename, 'w') as file:
        json.dump(data, file, indent=4)


def get_active_users_from(room_id):
    with open(rooms_json_filename, 'r') as file:
        data = json.load(file)
        rooms = data['rooms']
        for i in range(len(rooms)):
            if rooms[i]['id'] == room_id:
                return rooms[i]['active_users']


def restore_default_room_settings():
    default_room_settings = {'rooms': [{'name': 'Admin Room', 'id': 'AdminRoom', 'href': 'rooms/AdminRoom', 'active_users': []}]}
    with open(rooms_json_filename, 'w') as file:
        json.dump(default_room_settings, file, indent=4)