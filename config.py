import os
'''
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
'''

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bleh'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:mysecretpassword@localhost/jwtapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY='jeejptm'
