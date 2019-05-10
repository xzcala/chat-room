Project 3
========================================================================
by: Jon Basa

5/1/2019

### Introduction

This is the source code for Project 3 for the course CS4850. It includes a client and server code that allows multiple clients to have an online conversation through the use of Flask-SocketIO's socket function.


### Dependencies

These packages are used for this project:

* [Flask](http://flask.pocoo.org/ "Flask")
	: * provides the framework for the web application

* [Flask-Login](https://flask-login.readthedocs.io/en/latest/ "Flask-Login")
	: *  an extension that provides functions for user session management

* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/ "Flask-SQLAlchemy")
	: * an extension that provides database support

* [bulma ](https://cdnjs.com/libraries/bulma "bulma")
	: * the stylesheet used to style the web application

### How to run

The system running the server must have Python and pip installed. 

Open a CLI and change to the project directory and run the pip command: pip install -r requirements.txt

Then, run the project with the Python command: python chat.py

Open a browser and go to localhost:15400 to access the application as a client.

### Project Requirements

This section explains how each requirement is implemented in the code.

* port
	: The port is set implicitly when running the application.
	: Line 60 of chat.py: socketio.run(app, host='localhost', port=15400, use_reloader=False)
	: The sockets being created on the client side also connects to that port.	

* login
	: Flask-SQLAlchemy is used to create a database, with the model created in chat.py that holds user credentials such as their username and password. When the login form is filled, a query is sent to check if the user exists and sends an error message should the server decline it. 
	: see: lines 10-35 of auth.py
	
* newuser
	: The same database is used for creating new accounts. A form must be filled out by the user, and the server sends a query to check if the user already exists. The webpage returns an error message should a user attempt to create an account that already exists, or use a username or password that is too weak.
	: see: lines 37-61 of auth.py

* send
	: A user is able to send a message with text input and is sent to the server to be broadcasted to all connected hosts.
	: see: lines 10-24 of chat.html
	
* logout
	: A user must be logged in to have access to the logout function. logout_user() is called to log the user out of the chat room.
	: see: lines 63-68 of auth.py
	
### Issues

This section explains some issues with the program and general to-dos

* number of clients
	: Currently, the number of users able to connect is handled by Flask-Login. Need to somehow be able to limit it to three connections to fit project requirements.
	
* list of users
	: Need a section inside the chat room that lists all the current users online.
	
* private messages
	: Need to implement a way to send a message to one user.
	: Possible solutions: creating a "private" space that does not broadcast to all users.
	
* adjust flex boxes
	: The current layout between all the pages need to be unified as each page contains elements varying in size and color.
	: Possible solutions: create the containers inside base.html and only write inside blocks for the rest of the templates.

* fix nav-bar
	: Current nav-bar does not display if the screen is small.
	
* indicate user logout
	: Show a message on screen when a user signs out.