from coding_challenge_restful.basemodel import BaseModel
from coding_challenge_restful.models import Banks


class BankMethods(BaseModel):
    model = Banks

    @classmethod
    def get_all_records_paginated(cls, db, filters, limit=99999999999, offset=0):
        query = db.query(cls.model)
        for filter_param in filters:
            if filter_param == "id":
                query = query.filter(cls.model.id == filters[filter_param])
                continue
            elif filter_param == "name":
                query = query.filter(cls.model.name == filters[filter_param])
                continue
        query = query.limit(limit)
        query = query.offset(offset)
        return query.all()

