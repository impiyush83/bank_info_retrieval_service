import datetime
from functools import wraps
from flask import current_app as app, request
import jwt

from coding_challenge_restful.utils.custom_exceptions import AuthenticationException


def get_payload_from_jwt_token(token):
    try:
        payload = jwt.decode(
            token,
            app.config.get('APP_REQUEST_AUTH_SECRET'),
            algorithms='HS256'
        )
        if payload.get('unique_identifier') == "UNIQUE_APP":
            return payload
        return None
    except:
        return None


def generate_jwt_auth_token(user_id):
    # five days time delta
    five_days_expiration = datetime.timedelta(seconds=432000)
    five_days_expiration = datetime.datetime.utcnow() + five_days_expiration
    payload = dict(
        user_id=user_id,
        unique_identifier="UNIQUE_APP",
        exp=five_days_expiration
    )
    token = jwt.encode(
        payload,
        app.config.get('APP_REQUEST_AUTH_SECRET'),
        algorithm='HS256'
    ).decode('utf-8')
    return token


def authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        if not get_payload_from_jwt_token(auth_token):
            raise AuthenticationException("Invalid JWT Token")
        return func(*args, **kwargs)
    return wrapper
