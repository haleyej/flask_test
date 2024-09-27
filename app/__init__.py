from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

# creates an instance of a Flask object
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# bottom import avoids circular import problem
# routes handles different URLS
from app import routes, models