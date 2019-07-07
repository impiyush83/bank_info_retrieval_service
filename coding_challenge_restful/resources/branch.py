from flask import current_app as app, request
from flask_restful import Resource

from coding_challenge_restful.auth import authentication
from coding_challenge_restful.core.bank import get_all_branches
from coding_challenge_restful.utils.exceptions import exception_handle


class Branch(Resource):

    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    @authentication
    def get(self, city, bank_name):
        """

    .. http:get::  /bank/<city>/<bank_name>/branches?q=limit=25&offset=25

       This api will be used to return all branches of the the bank name in specific city.

        **Example request**:

        .. sourcecode:: http

           GET  /bank/<city>/<bank_name>/branches?q=limit=25&offset=25  HTTP/1.1

        **Example response**:

        {
            "branches": [
                {
                    "city"
                },
                {

                }
            ]
        }


        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        branches = get_all_branches(city, bank_name, limit, offset)
        return {"branches": branches}, 200
