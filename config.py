import os
basedir = os.getcwd()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:29403241@localhost/bigdata'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://ktkpyrovtglcnz:0ef4c7e58a874cb3a807a7109dd274929483a4ded20cec7a7fa28f9a68e74adc@ec2-54-243-185-123.compute-1.amazonaws.com:5432/dfrf1v1b6c59d9'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}