from flask import Blueprint
from flask_restful import Api

from users.resources import UserResource

user_app = Blueprint('users', __name__, url_prefix='/users')
api = Api(user_app)

api.add_resource(UserResource, '')