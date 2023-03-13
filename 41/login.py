from functools import wraps

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get("user", None) or args[0]
        if user in loggedin_users:
            return func(*args, **kwargs)
        elif user in known_users:
            return "please login"
        else:
            return "please create an account"

    return wrapper


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    return f"welcome back {user}"
