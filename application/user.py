from flask_login import UserMixin


#   Database needs to support other values for user:
#   email, admin, moderator, banned, member_since


class User(UserMixin):
    def __init__(self, name, id):
        self.username = name
        self.id = id

    @property
    def is_authenticated(self):
        return True

    @property
    def is_admin(self):
        return True

    @property
    def is_moderator(self):
        return True

    