from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure key in production
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # Configure the database URI. the f' helps
	# to create a string with the value of DB_NAME, which is 'database.db'. So the final URI will be
	# 'sqlite:///database.db'
	db.init_app(app)  # Initialize the database with the Flask app
	
	from .view import view
	from .auth import auth
	
	app.register_blueprint(view, url_prefix='/')  # Register the view blueprint with the app
	app.register_blueprint(auth, url_prefix='/')  # Register the auth blueprint with the app
	#from website import models
	from .models import User, Note, AuthenticationToken
	# Import the User and Note models to create the database tables
	
	create_database(app)
	
	return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
