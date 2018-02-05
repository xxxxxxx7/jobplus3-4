from flask import Flask
from jobplus.config import configs
from flask_migrate import Migrate
from jobplus.models import db,User,Company
from flask_login import LoginManager


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

    login_manager = LoginManager()
    # 设置安全级别 None、'basic'、'strong'
    # flask_login 会记住客户端的IP地址和用户代理信息
    login_manager.session_protection="strong"

    login_manager.init_app(app)

    # 这是回调函数
    # 登录验证时LoginManger从数据库加载用户
    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    # 指定登录视图
    login_manager.login_view = 'front.login'


def register_blueprints(app):
    from .handlers import front, user, company

    app.register_blueprint(front)
    app.register_blueprint(user)
    app.register_blueprint(company)
