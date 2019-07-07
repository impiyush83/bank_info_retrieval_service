import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    COUNTRY_NAME = 'INDIA'
    COUNTRY_TIME_ZONE = 'Asia/Kolkata'
    DATABASE_URL = os.environ.get('DATABASE_URL',
                                  default='postgres://tlklkcimykmfha:cf7f038851a2bca9499c224ac2e97aab20b979970dca7391d'
                                          'cd01328cb617c39@ec2-23-21-160-38.compute-1.amazonaws.com:5432/d7lf2brvmaetv9'
                                  )
    APP_REQUEST_AUTH_SECRET = "MySecretKeyForJwtToken"
    JWT_ACCESS_TOKEN_EXPIRES = 432000
