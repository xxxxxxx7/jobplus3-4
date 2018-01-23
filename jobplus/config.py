import os


class BaseConfig():
    SECRET_KEY = 'ABCabc'


class DevelopmentConfig(BaseConfig):
    path = os.path.join(os.getcwd(), 'jobplus.db').replace('\\', '/')
    # SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(path)
    SQLALCHEMY_DATABASE_URI='mysql://root@localhost/jobplus?charset=utf8'
    DEBUG = 1


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI='mysql://root@localhost/jobplus?charset=utf8'
    DEBUG = 0


configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }


