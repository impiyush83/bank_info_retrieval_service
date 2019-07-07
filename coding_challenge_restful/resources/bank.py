from flask import current_app as app, request
from flask_restful import Resource

from coding_challenge_restful.auth import authentication
from coding_challenge_restful.core.bank import get_bank_details
from coding_challenge_restful.utils.exceptions import exception_handle


class Bank(Resource):

    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    @authentication
    def get(self, ifsc):
        """

        .. http:get::  /bank/branch/<ifsc>?q=limit=25&offset=25

        This api will be used to return bank details of the IFSC Code.

        **Example request**:

        .. sourcecode:: http

           GET  /bank/branch/<ifsc>?q=limit=25&offset=25  HTTP/1.1

        **Example response**:


            {
                "bank_name" : "Bank Name",
                "bank_id" : "Bank_id"
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
        bank_details = get_bank_details(ifsc, limit, offset)
        return bank_details, 200
