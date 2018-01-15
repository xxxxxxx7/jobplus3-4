from flask import Flask
from jobplus.config import configs


def create_app(config):
    app = Flask(__name__)
    
    app.config.from_object(configs.get(config))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0

    return app


