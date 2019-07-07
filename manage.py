from coding_challenge_restful.app import create_app
from coding_challenge_restful.settings import Config
from flask_script import Manager, Server

app = create_app(Config)

manager = Manager(app=app)
manager.add_command('server', Server(threaded=True))

manager.run()
