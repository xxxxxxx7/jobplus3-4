import os


class BaseConfig():
    SECRET_KEY = 'ABCabc'
    INDEX_PER_PAGE = 6


class DevelopmentConfig(BaseConfig):
    path = os.path.join(os.getcwd(), 'jobplus.db').replace('\\', '/')
    # SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(path)
    SQLALCHEMY_DATABASE_URI='mysql://root:root@127.0.0.1/jobplus?charset=utf8'
    DEBUG = 1


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI='mysql://root@127.0.0.1/jobplus?charset=utf8'
    DEBUG = 0


configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }


