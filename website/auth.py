from flask import Blueprint, render_template

# "Blueprint" of application -> a way to organize a group of related views and other code.


auth = Blueprint('auth', __name__)


@auth.route('/login')  # login page
def login():
	#   return render_template('login.html', text="Test", user="Donika")
	
	#	return render_template('login.html', boolean=True) # if statment in login.html will be true and show the text
	#	"You are logged in" instead of "You are not logged in"
	
	return render_template('login.html')


@auth.route('/logout')  # logout page
def logout():
	return "<p> Logout </p>"


@auth.route('/sign-up')  # sign up page
def sign_up():
	# return "<p> Sign Up </p>"
	return render_template('sign_up.html')
