from app import app

if __name__ == '__main__':
	# socketio.run(app, port=app.config['PORT'], host='0.0.0.0', debug=True)
	app.run(port=app.config["PORT"], debug=app.config["DEBUG"])