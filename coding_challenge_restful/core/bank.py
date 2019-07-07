from coding_challenge_restful.extensions import db
from coding_challenge_restful.model_methods.bank_methods import BankMethods
from coding_challenge_restful.model_methods.branches_methods import BranchesMethods
from coding_challenge_restful.utils.custom_exceptions import NoResultFound
from coding_challenge_restful.utils.utils import rows_to_list, row_to_dict


def get_bank_details(ifsc, limit, offset):
    banks = BranchesMethods.get_all_records_paginated(db, dict(ifsc=ifsc))
    if len(banks) == 0:
        raise NoResultFound("Search results not found")
    bank_id = banks[0].bank_id
    bank_details = BankMethods.get_all_records_paginated(db, dict(id=bank_id), limit=limit, offset=offset)
    if len(bank_details) == 0:
        raise NoResultFound("Search results not found")
    bank_details = row_to_dict(bank_details[0])
    return bank_details


def get_all_branches(city, bank_name, limit, offset):
    bank_details = BankMethods.get_all_records_paginated(db, dict(name=bank_name))
    if len(bank_details) == 0:
        raise NoResultFound("Search results not found")
    bank_details = bank_details[0]
    bank_id = bank_details.id
    branches = BranchesMethods.get_all_records_paginated(db, dict(city=city, bank_id=bank_id), limit=limit, offset=offset)
    branches = rows_to_list(branches)
    return branches
