from flask import Flask
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask('book-test-flask', template_folder="templates")
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.add_url_rule('/<path:filename>', endpoint='route',view_func=app.send_static_file)

CORS(app)
db = SQLAlchemy(app)

from models import Database
database = Database.getInstance()

##
## INDEX ##########################################################################################
##

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
	resp = None
	if request.method == 'GET':
		resp = make_response(render_template('add_book.html')), 200
	elif request.method == 'POST':
		title = request.form['title']
		author = request.form['author']

		database.add_book(title = title, author = author)
		resp = make_response(render_template('add_book.html')), 200
	return resp


@app.route('/bookstore', methods=['GET'])
def bookstore():
	books = database.get_books()

	return render_template('bookstore.html', data=books)


@app.route('/file_uploader', methods=['GET', 'POST'])
def file_uploader():
	resp = None
	if request.method == "GET":
		resp = make_response(render_template('file_uploader.html')), 200
	elif request.method == "POST":
		file = request.files['file']
		print(file.filename)
		resp = make_response(render_template('file_uploader.html')), 200

	return resp

@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return send_from_directory('static', 
    	'images/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')