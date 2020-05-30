from users.models import User


def get_all_users():
    return User.get_all()


def create_user(user):
    user.save()
    return user
