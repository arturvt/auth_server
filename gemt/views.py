from gemt import app
from flask import jsonify, request

help_app = ['Welcome to GEMT Reader server.']


@app.route('/', methods=['GET'])
def index():
    return '<br>'.join(help_app)


@app.route('/read_keys', methods=['GET'])
def get_devices_info():
    return jsonify({'Keys': 'Show Call Read Keys Function'})