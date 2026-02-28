from website import create_app

app = create_app()
if __name__ == '__main__':  # only if we run this file are we going to execute this file
	app.run(
		debug=True
		)  # Enable debug mode for development (remove in production), auto-reloads the server on code changes

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():  # put application's code here
#	return 'Hello World!'
# if __name__ == '__main__':
#	app.run()
