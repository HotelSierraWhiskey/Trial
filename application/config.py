import os
import json


def _get(item):
    fname = "settings.json"
    if fname in os.listdir():
        settings = open('settings.json')
        data = json.load(settings)
        return data[item]
    else:
        raise FileNotFoundError


config = {
    'SECRET_KEY': _get("secret_key"),
    'SQLALCHEMY_DATABASE_URI': f"mysql+pymysql://{_get('database_user')}:{_get('database_password')}@localhost/trial",
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}