from flask import Blueprint, flash, redirect, render_template, request, url_for

# "Blueprint" of application -> a way to organize a group of related views and other code.

from .models import User  # Import the User model from the models module to interact with user data in the database
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Import the db object from the current package to interact with the database

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])  # login page
def login():
	"""
	Just some code snippets for reference:
	return render_template("login.html", text="Test", user="Donika")
	return render_template("login.html", boolean=True) # if statement in login.html will be true and show the text
	You are logged in" instead of "You are not logged in"
	"""
	
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		
		user = User.query.filter_by(email=email).first()
		if user:
			if check_password_hash(user.passwordHash, password):
				flash('Logged in successfully!', category='success')
				return redirect(url_for('view.home'))
			else:
				flash('Incorrect password, try again.', category='error')
		else:
			flash('Email does not exist.', category='error')
			
			return redirect(url_for('view.home'))
		
	return render_template('login.html')



'''# email = request.form.get("email")
# password = request.form.get("password")

# TODO:
# - Add email and password validation
# - Check credentials against the database
# - Implement session management'''



@auth.route('/logout')
def logout():
	# TODO: Clear session/logout user
	return redirect(url_for('view.home'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		email = request.form.get('email')
		firstName = request.form.get('firstName')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		
		user = User.query.filter_by(email=email).first()
		if user:
			flash('Email already exists.', category='error')
		if len(email) < 5:
			flash('Email must be at least 5 characters long.', category='error')
		elif len(firstName) < 2:
			flash('First name must be at least 2 characters long.', category='error')
		elif password1 != password2:
			flash('Passwords do not match.', category='error')
		elif len(password1) < 7:
			flash('Password must be at least 7 characters long.', category='error')
		else:
			new_user = User(
				email=email, firstName=firstName, passwordHash=generate_password_hash(
					password1,
					method="pbkdf2:sha256"
					)
				)
			db.session.add(new_user)
			db.session.commit()
			
			flash("Account created successfully!", category='success')
			
			return redirect(url_for('view.home'))
	
	return render_template('sign_up.html')
	
	''' Just some code snippets for reference:
		#data = request.form
		#email = data.get('email')
		#password = data.get('password') '''
