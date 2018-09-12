import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    WTF_CSRF_ENABLED = False
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///t247_dev'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False
    DB_NAME = "da413jdbc3tdcb"
    # DATABASE_URL = os.environ['DATABASE_URL']
    DATABASE_URL = "postgres://dtmqgqimaattms:3ff5ee89510c06f7dd95d40ae2d0e3cfaee6f4c1156182ae810eb91d5e438576@ec2-54-235-252-137.compute-1.amazonaws.com:5432/da413jdbc3tdcb"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
