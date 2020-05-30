from flask import request
from flask_restful import Resource

from orm import db
from users.manager import get_all_users, create_user
from users.schemas import UserSchema


class UserResource(Resource):
    @classmethod
    def get(cls):
        users = get_all_users()
        serialized_data = UserSchema(many=True).dump(users)
        return serialized_data

    @classmethod
    def post(cls):
        data = UserSchema().load(request.json, session=db.session)
        user = create_user(data)
        serialized_data = UserSchema().dump(user)
        return serialized_data