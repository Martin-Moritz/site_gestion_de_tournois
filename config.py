"""App configuration."""
import os
from os import environ

class Config(object):

    #General Config
    SECRET_KEY='you-will-never-guess-the-secret-key-01'
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
