# The Application initialization file
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Basic Flask + SqlAlchemy initialization
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# Add routes and models here so the App has access to endpoints and database entities:
from src.models import usermodel
from src.routes import loginroute