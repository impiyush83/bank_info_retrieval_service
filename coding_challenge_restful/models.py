# Models are defined here
from sqlalchemy import Column, Integer, String, ForeignKey

from coding_challenge_restful.extensions import Model


# Define models here
class Banks(Model):
    __tablename__ = "banks"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(49))


class Branches(Model):
    __tablename__ = "branches"

    ifsc = Column(String(11), nullable=False, primary_key=True)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    branch = Column(String(74))
    address = Column(String(195))
    city = Column(String(50))
    district = Column(String(50))
    state = Column(String(50))


class User(Model):
    __tablename__ = "bank_user"

    user_id = Column(String(256), primary_key=True)
    password = Column(String(256), nullable=False)
