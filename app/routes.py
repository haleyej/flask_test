from app import app 
from flask import render_template

# view functions mapped to 1+ URLS
# Flask knows what to execute when the client requests a URL


# A decorator modifies the function that follows it 
# Creates an association between the URLS and the function
@app.route('/')
@app.route('/index')
def index():
    # mock user and post objects while we build out logic
    user = {'username': 'Haley'}
    posts = [
        {
            'author': {'username': 'John'}, 
            'body': 'Beautiful day in Portland'
        }, 
        {'author': {'username': 'Susan'}, 
         'body': 'My review of Challengers'}
    ]

    return render_template('index.html', title = 'Home', user = user, posts = posts)