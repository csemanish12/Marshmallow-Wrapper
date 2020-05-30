from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from users.models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User

    name = fields.Str(required=True)
