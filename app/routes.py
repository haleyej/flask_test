from app import app 
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # does all the processing work
    # returns true if form does not fail
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title = 'Sign In', form = form)