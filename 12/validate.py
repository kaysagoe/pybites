from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    def __init__(self):
        super()


class UserAccessExpired(Exception):
    def __init__(self):
        super()


class UserNoPermission(Exception):
    def __init__(self):
        super()


def get_secret_token(username):
    users_dict = {user.name: user for user in USERS}

    if not (found_user := users_dict.get(username, None)):
        raise UserDoesNotExist()

    if found_user.expired:
        raise UserAccessExpired()

    if found_user.role != ADMIN:
        raise UserNoPermission()

    return SECRET
