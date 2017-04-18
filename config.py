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
    SQLALCHEMY_DATABASE_URI = 'postgres://toppqsvvpcgceh:8e560b0767dc6b30d5140589013a2baca8752165a642c8188459ca806176fa4c@ec2-54-243-252-91.compute-1.amazonaws.com:5432/da1ftjs8usjpu0'



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}