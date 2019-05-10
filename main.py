# this file creates the  blueprint for the default route

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# create the blueprint of the default routes
main = Blueprint('main', __name__)

# route for the landing page
@main.route('/')
def index():
    return render_template('index.html')

# route for the chat room page, the user must be signed in to access it
@main.route('/chat')
@login_required
def chat():
	return render_template('chat.html', username=current_user.id)

# route for the about page, the user must be signed in to access it	
@main.route('/about')
@login_required
def about():
	return render_template('about.html')