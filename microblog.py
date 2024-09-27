#top level script to define a Flask instance
import sqlalchemy as sa 
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# decorator registers functions as shell context fns
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 
            'so': so, 
            'db': db, 
            'User': User, 
            'Post': Post}