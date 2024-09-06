from flask import Flask 
from config import Config

# creates an instance of a Flask object
app = Flask(__name__)
app.config.from_object(Config)

# bottom import avoids circular import problem
# routes handles different URLS
from app import routes 