from flask import Blueprint, flash, redirect, render_template, request, url_for

# "Blueprint" of application -> a way to organize a group of related views and other code.

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
        data = request.form
        email = data.get('email')
        password = data.get('password')

    # TODO: Add email and password validation
    # TODO: Check credentials against database
    # TODO: Implement session management

    return render_template('login.html')


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

        if len(email) < 5:
            flash('Email must be at least 5 characters long.', category='error')
        elif len(firstName) < 2:
            flash('First name must be at least 2 characters long.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters long.', category='error')
        else:
            flash("Account created successfully!", category='success')
            # add user to database
            return redirect(url_for('view.home'))

    return render_template('sign_up.html')
    
    
    ''' Just some code snippets for reference:
		#data = request.form
		#email = data.get('email')
		#password = data.get('password') '''
