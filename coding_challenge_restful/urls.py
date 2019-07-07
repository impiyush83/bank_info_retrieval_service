from coding_challenge_restful.resources.access_token import AccessToken
from coding_challenge_restful.resources.bank import Bank
from coding_challenge_restful.resources.branch import Branch
from coding_challenge_restful.utils import URLS
urls = [
    URLS(resource=AccessToken, endpoint=['access-token'], name='get_access_token'),
    URLS(resource=Bank, endpoint=['bank/branch/<string:ifsc>'], name='get_bank_details_with_ifsc'),
    URLS(resource=Branch, endpoint=['bank/<string:city>/<string:bank_name>/branches'], name='get_all_branches'),
]
