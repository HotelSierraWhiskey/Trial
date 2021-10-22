from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, name, id):
        self.username = name
        self.id = id

    def is_authenticated(self):
        return True