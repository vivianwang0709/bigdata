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
    SQLALCHEMY_DATABASE_URI = 'postgres://qpshpdiojmrkec:790073148c28f9626dc6a606655df2385d02e699bc12dc03c508a46e4dddbf00@ec2-54-235-168-152.compute-1.amazonaws.com:5432/d3s2cchcra5038'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}