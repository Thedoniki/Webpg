from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
	
	return app
