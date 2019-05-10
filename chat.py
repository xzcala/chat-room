from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_socketio import SocketIO, send
import datetime

# create the Flask application and define config values. the key is for accessing the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = '/8h3<I0"RXGK}[p'
#app.debug = False

# create the database needed to store user credentials
db = SQLAlchemy(app)

# create model for the database
class User(UserMixin, db.Model):
	# credentials a User will be using to sign in
	# while the lab asks to use UserID, I am simplifying to id to save a few lines of code as flask_login needs a primary key named id to associate with a cookie @line27 main.py
	id = db.Column(db.String(32), unique=True, nullable=False, primary_key=True)
	Password = db.Column(db.String(100))
	
	# other information
	created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	last_active_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# create a SocketIO
socketio = SocketIO(app)

# initialize the login manager which contains the code that lets the application and the flask-login extension to work together. the login_view value sets the location if the user is not authenticated/needs to sign in
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# create a list of users
users = {}

# this function tells flask_login how to handle the request
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

# this function is used to send a message to the chat room
@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

# blueprint which sets the route for authentication, if the user wants to login or signup
from auth import auth
app.register_blueprint(auth)

# blueprint which sets the default route
from main import main
app.register_blueprint(main)

# create database and run socketio on the port required by the project
if __name__ == '__main__':
	db.create_all()
	socketio.run(app, host='localhost', port=15400, use_reloader=False)