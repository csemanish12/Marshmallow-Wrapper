from flask import Flask

from error_handlers import errors
from jsontool import marshmallow
from orm import db
from users.app import user_app


def initialize_error_handler(app):
    app.register_blueprint(errors)


def initialize_blueprints(app):
    app.register_blueprint(user_app)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    marshmallow.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    initialize_error_handler(app)
    initialize_blueprints(app)
    return app