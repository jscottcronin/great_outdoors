from flask import Flask, render_template, request, jsonify, abort
from app.test_data import test_data
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/site_id/<int:site_id>')
def get_data_for_siteid(site_id):
    print(type(site_id))
    # show the user profile for that user
    return jsonify(test_data)
