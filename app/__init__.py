from flask import Flask 

# creates an instance of a Flask object
app = Flask(__name__)

# bottom import avoids circular import problem
# routes handles different URLS
from app import routes 