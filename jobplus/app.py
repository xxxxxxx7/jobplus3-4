from flask import Flask
from jobplus.config import configs
from flask_migrate import Migrate
from jobplus.models import db,User,Company

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0
    
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)


def register_blueprints(app):
    from .handlers import front

    app.register_blueprint(front)
