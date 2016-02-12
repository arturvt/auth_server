from gemt import app
from flask import jsonify, request
from gemt.data.database import get_all
from controller import KeysHandler

help_app = ['Welcome to GEMT Reader server.']


class ParametersValidationException(Exception):
    pass


def validate_schema(mandatory, optional=None):
    """
    Validates a JSON Schema according to a list of mandatory and optional items.
    If any mandatory is not present then it raises an exception
    If optional is not None and all items in optional is not present them it raises and exception
    :param mandatory:
    :param optional:
    :return:
    """
    if not request.json or any(m not in request.json for m in mandatory):
        raise ParametersValidationException()
    if optional and not any(t in request.json for t in optional):
        raise ParametersValidationException


@app.route('/', methods=['GET'])
def index():
    return '<br>'.join(help_app)


@app.route('/help', methods=['GET'])
def index():
    return '<br>'.join(help_app)


@app.route('/get_all', methods=['GET'])
def get_all_content():
    return jsonify({'All': get_all()})


@app.route('/add', methods=['POST'])
def add_key():
    validate_schema(mandatory=['key_value'])
    return jsonify({'Result': KeysHandler(request.json['key_value']).add_key()})


@app.route('/check/<string:key_value>', methods=['PUT'])
def check_key(key_value):
    validate_schema(mandatory=['machine_id'])
    return jsonify({'Result': KeysHandler(key_value).validate_key(request.json['machine_id'])})


@app.route('/authenticate/<string:key_value>', methods=['PUT'])
def authenticate_key(key_value):
    validate_schema(mandatory=['machine_id'])
    return jsonify({'Result': KeysHandler(key_value).authenticate_key(request.json['machine_id'])})