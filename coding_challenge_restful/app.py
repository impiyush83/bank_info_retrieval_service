import os

from flask import Flask
from flask_jwt_extended import JWTManager

from coding_challenge_restful.flask_restful_api import restful_api


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.urandom(24)
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    restful_api(app)
    jwt = JWTManager(app)
    return app
