from coding_challenge_restful.extensions import db


class BaseModel:
    model = None

    @classmethod
    def create_record(cls, values):
        obj = cls.model(**values)
        db.add(obj)
        db.flush()
        return obj
