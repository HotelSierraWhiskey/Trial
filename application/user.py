from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, name, id):
        self.name = name
        self.id = id