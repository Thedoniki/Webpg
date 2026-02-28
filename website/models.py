from . import db  # from the current package, import the db object that we created in __init__.py

from flask_login import UserMixin  # import UserMixin from flask_login,
# which provides default implementations for user authentication methods

from sqlalchemy.sql import func  # imported for date column in class Note


class AuthenticationToken(db.Model):  # Define an AuthenticationToken model that inherits from db.Model, which will
	# represent the authentication tokens in our database. This model will be used to store tokens for user
	# authentication and session management.
	tokenID = db.Column(db.Integer, primary_key=True)
	userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)
	tokenHash = db.Column(db.String(150), nullable=False)
	tokenType = db.Column(db.String(150), nullable=False)
	issuedAt = db.Column(db.DateTime(timezone=True), default=func.now())


class Note(db.Model):  # Define a Note model that inherits from db.Model, which will represent the notes in our
	# database. This will be a more general db model.
	noteID = db.Column(db.Integer, primary_key=True)  # For all obj. need a PK for unique identification.
	# By def, you don't need to define an id on a new obj, software smart enough to auto-increment the id for each new
	# obj. So we can just create a new note without specifying the id, and it will automatically get a unique id.
	content = db.Column(db.String(10000))  # changed var from data to content............The content of the note,
	# which is a string with a max length of 10,
	# 000 characters.
	createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
	# SqlAlchemy will automatically set the date to the
	# current date and time when a new note is created, using func.now().
	userID = db.Column(db.Integer, db.ForeignKey('user.userID'))  # USER.ID REFERS TO CLASS USER and field id in that


# class. FK, a column in your db that refers to another table.
# Because of Fk, you must pass a valid id of an existing user when creating a new note/object. Since 1 user can
# have many notes. The FK is the child obj that ref. the parent obj. This establishes a relationship between the
# Note and User


class User(db.Model, UserMixin):  # Define a User model that inherits from db.Model and UserMixin,
	# Usermixin is added only for user object. It provides default implementations for user authentication methods,
	# such as is_authenticated, is_active, and get_id. This model will represent the users in our database and will be
	# used for authentication and user management.
	
	# below, defining the schema for the User model, which includes the following fields / columns:
	userID = db.Column(db.Integer, primary_key=True)  # For all obj. need a PK for unique identification.
	# so the id field is an integer and is the primary key of the User table.
	email = db.Column(db.String(150), unique=True)  # User's email address max length 150, must be unique
	passwordHash = db.Column(db.String(150))  # User's password (should be hashed in production)
	firstName = db.Column(db.String(150))  # User's first name
	
	# Below, establish a relationship between User and Note models. So user can find all their notes.
	# We can access a user's notes using user.notes. The relationship is defined on the User model,
	# and it references the Note model.
	notes = db.relationship('Note')  # Tells flask and SQL Alcamy, every time  an note is created also add that note
# ID to notes=db.relationship('Note') in the User class. So we can access a user's notes using user.notes,
# #which will return a list of all the notes associated with that user.
