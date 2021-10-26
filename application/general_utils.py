import json
from .admin_utils import rooms_json_filename


def get_room_name_from_id(room_id):
    with open(rooms_json_filename, 'r') as file:
        data = json.load(file)
        rooms = data['rooms']
        for room in rooms:
            if room['id'] == room_id:
                return room['name']
        return None


def get_room_id_from_name(name):
    with open(rooms_json_filename, 'r') as file:
        data = json.load(file)
        rooms = data['rooms']
        for room in rooms:
            if room['name'] == name:
                return room['id']
        return None