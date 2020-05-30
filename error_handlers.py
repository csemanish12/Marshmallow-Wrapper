from flask import jsonify, Blueprint
from marshmallow import ValidationError

from exceptions import AppValidationError


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(ValidationError)
def validation_error(error):
    app_validation_error = AppValidationError(error.messages).to_dict()
    return jsonify(app_validation_error), app_validation_error['code']
