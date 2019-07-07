from flask.config import Config
from sqlalchemy_wrapper import SQLAlchemy

config_name = 'coding_challenge_restful.settings.Config'
config = Config('')
config.from_object(config_name)

isolation_level = 'READ COMMITTED'
db = SQLAlchemy(
    uri=config['DATABASE_URL'],
    isolation_level=isolation_level
)
# Create Models
Model = db.Model

