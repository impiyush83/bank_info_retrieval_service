from coding_challenge_restful.basemodel import BaseModel
from coding_challenge_restful.models import Branches


class BranchesMethods(BaseModel):
    model = Branches

    @classmethod
    def get_all_records_paginated(cls, db, filters, limit=99999999999, offset=0):
        query = db.query(cls.model)
        for filter_param in filters:
            if filter_param == "ifsc":
                query = query.filter(cls.model.ifsc == filters[filter_param])
                continue
            elif filter_param == "city":
                query = query.filter(cls.model.city == filters[filter_param])
                continue
            elif filter_param == "bank_id":
                query = query.filter(cls.model.bank_id == filters[filter_param])
                continue
            elif filter_param == "state":
                query = query.filter(cls.model.state == filters[filter_param])
                continue
            elif filter_param == "address":
                query = query.filter(cls.model.address == filters[filter_param])
                continue
        query = query.limit(limit)
        query = query.offset(offset)
        return query.all()
