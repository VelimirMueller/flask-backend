# Add app config here:
# Is connected to .flaskenv and can read its configurations and make them usable in Flask.
# usage: YOUR_APP_KEY = os.environ.get('YOUR_KEY_IN_FLASKENV')
import os

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')