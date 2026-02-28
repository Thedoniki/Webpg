from flask import Blueprint, render_template

# "Blueprint" of application -> a way to organize a group of related views and other code.


view = Blueprint('view', __name__)


@view.route('/')  # home page
def home():
	return render_template("home.html")  # Render the home.html template when the home page is accessed
