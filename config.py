import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:anna@localhost/TuasWorkspaces'

    SQLALCHEMY_TRACK_MODIFICATIONS = False