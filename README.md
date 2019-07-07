***HOSTING INFORMATION***

https://fyle-bank-service.herokuapp.com/


**API DOCS**

1. Get 5 days valid access token

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
        
2. Bank Details with specific IFSC code

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
        
3. Branches with City and bank name.

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
                    "state": "MAHARASHTRA",
                    "city": "MUMBAI",
                    "branch": "BAIL BAZAR",
                    "ifsc": "ABHY0065003",
                    "district": "GREATER MUMBAI",
                    "address": "KMSPM'S SCHOOL, WADIA ESTATE, BAIL BAZAR-KURLA(W), MUMBAI-400070",
                    "bank_id": 60
                },
                {
                    "state": "MAHARASHTRA",
                    "city": "MUMBAI",
                    "branch": "BHANDUP",
                    "ifsc": "ABHY0065004",
                    "district": "GREATER MUMBAI",
                    "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
                    "bank_id": 60
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
    
**Real Examples**

1. Get 5 days valid access token

        """

        .. http:get::  https://fyle-bank-service.herokuapp.com/access-token

        This api will be used to create profile of user

        **Example request**:

        .. sourcecode:: http

           GET  /access-token  HTTP/1.1

        **Example response**:

        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMSIsInVuaXF1ZV9pZGVudGlmaWVyIjoiVU5JUVVFX0FQUCIsImV4cCI6MTU2Mjk2MjE1MH0.dwGOm9zQ0IqIYo8GSkviL7rZRAR7CSFAPhhnIM3XSiA"
        }

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        
2. Bank Details with specific IFSC code

        """

        .. http:get::  /bank/branch/ABHY0065001?q=limit=25&offset=0

        This api will be used to return bank details of the IFSC Code.

        **Example request**:

        .. sourcecode:: http

           GET  https://fyle-bank-service.herokuapp.com/bank/branch/<ifsc>?q=limit=25&offset=25  HTTP/1.1

        **Example response**:


            {
                "bank_id": 60,
                "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
            }


        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error

        """
        
3. Branches with City and bank name.

        """

        .. http:get::  /bank/MUMBAI/ABHYUDAYA COOPERATIVE BANK LIMITED/branches?limit=2&offset=2

       This api will be used to return all branches of the the bank name in specific city.

        **Example request**:

        .. sourcecode:: http

           GET  https://fyle-bank-service.herokuapp.com/bank/<city>/<bank_name>/branches?q=limit=25&offset=25  HTTP/1.1

        **Example response**:

        {
            "branches": [
                {   
                    "state": "MAHARASHTRA",
                    "city": "MUMBAI",
                    "branch": "BAIL BAZAR",
                    "ifsc": "ABHY0065003",
                    "district": "GREATER MUMBAI",
                    "address": "KMSPM'S SCHOOL, WADIA ESTATE, BAIL BAZAR-KURLA(W), MUMBAI-400070",
                    "bank_id": 60
                },
                {
                    "state": "MAHARASHTRA",
                    "city": "MUMBAI",
                    "branch": "BHANDUP",
                    "ifsc": "ABHY0065004",
                    "district": "GREATER MUMBAI",
                    "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
                    "bank_id": 60
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