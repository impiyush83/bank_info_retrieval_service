from flask import current_app as app
from flask_restful import Resource

from coding_challenge_restful.core.access_token import get_access_token
from coding_challenge_restful.utils.exceptions import exception_handle


class AccessToken(Resource):

    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        """

        .. http:get::  /access-token

        This api will be used to create profile of user

        **Example request**:

        .. sourcecode:: http

           GET  /access-token  HTTP/1.1

        **Example response**:

        {
            "token": 'secret-token-key'
        }

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        access_token = get_access_token()
        return {"token": access_token}, 200
