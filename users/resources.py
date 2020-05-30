from flask import request
from flask_restful import Resource

from orm import db
from users.manager import get_all_users, create_user
from users.schemas import UserSchema
from wrappers.marshmallow.serializer import Serializer


class UserResource(Resource):
    @classmethod
    def get(cls):
        users = get_all_users()
        serialized_data = UserSchema(many=True).dump(users)
        return serialized_data

    @classmethod
    def post(cls):
        # using marshmallow 3
        # data = UserSchema().load(request.json, session=db.session)
        # user = create_user(data)
        # serialized_data = UserSchema().dump(user)

        # using marshmallow 2
        # data, errors = UserSchema(strict=True).load(request.json, session=db.session)
        # user = create_user(data)
        # serialized_data, error = UserSchema().dump(user)

        # using wrapper
        user_object = Serializer().deserialize(request.json, UserSchema, session=db.session)
        user = create_user(user_object)
        serialized_data = Serializer().serialize(user, UserSchema, session=db.session)
        return serialized_data