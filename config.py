import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'lab2.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:anna@localhost/TuasWorkspaces'

    SQLALCHEMY_TRACK_MODIFICATIONS = False