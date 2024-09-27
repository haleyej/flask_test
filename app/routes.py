from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app.models import User
from app.forms import LoginForm, RegistrationForm
from urllib.parse import urlsplit

# view functions mapped to 1+ URLS
# Flask knows what to execute when the client requests a URL


# A decorator modifies the function that follows it 
# Creates an association between the URLS and the function
# The login required decorator protects pages against annoymous view -- can only see if authenticated
@app.route('/')
@app.route('/index')
@login_required
def index():
    # mock user and post objects while we build out logic
    posts = [
        {
            'author': {'username': 'John'}, 
            'body': 'Beautiful day in Portland'
        }, 
        {'author': {'username': 'Susan'}, 
         'body': 'My review of Challengers'}
    ]
    return render_template('index.html', title = 'Home', posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # does all the processing work
    # returns true if form does not fail

    # handle if current user is already logged in 
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # query database to get user 
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        print('AUTHENTICATED')
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        print('VALIDATING')
        # add user info to database
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Congratulations! You are now a registered user')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)