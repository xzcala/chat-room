# this file creates the  blueprint for the authentication functions

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# create the blueprint of the authentication routes
auth = Blueprint('auth', __name__)

# route for login with an empty form
@auth.route('/login')
def login():
    return render_template('login.html')

# route for the login form the user will be submitting. the user is logged in after login_user is called and is redirected
@auth.route('/login', methods=['POST'])
def login_post():
	from chat import User, db
	# store user input for a comparison
	id = request.form.get('username')
	Password = request.form.get('password')
	remember = True if request.form.get('remember') else False

	# make sure user exists first by comparing it to the table using a query
	user = User.query.filter_by(id=id).first()

	# also check if password is correct, indicate user to try again if either has failed
	if not user or not check_password_hash(user.Password, Password):
		flash('Username or password is incorrect, try again!')
		return redirect(url_for('auth.login'))

	# creates a cookie and session for the user, letting the server know that they are currently online
	login_user(user)

	return redirect(url_for('main.chat'))

# route for creating a new account
@auth.route('/signup')
def signup():
    return render_template('signup.html')

# route for the sign up form the user will be submitting. it applies a hash algorithm to the password and calls query and session functions from the database library 
@auth.route('/signup', methods=['POST'])
def signup_post():
	from chat import User, db
	id = request.form.get('username')
	Password = request.form.get('password')

	# make sure user does not already exist, this query checks if there is a match
	user = User.query.filter_by(id=id).first()

	# if there is a match, reload the form and send a message
	if user:
		flash('Username is taken. Try again with a different name!')
		return redirect(url_for('auth.signup'))

	# else, make a new entry in the database by saving the username and password
	new = User(id=id, Password=generate_password_hash(Password, method='sha256'))
	db.session.add(new)
	db.session.commit()
	return redirect(url_for('auth.login'))

# route for logging out. the user must be signed in to do this action and calls the logout function from the flask_login library
@auth.route('/logout')
@login_required
def logout(): 
	logout_user()
	return redirect(url_for('main.index'))