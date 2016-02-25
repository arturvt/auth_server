from gemt import app
from flask import jsonify, request, abort
from gemt.data.database import get_all, get_free_content, get_summary, get_free_keys_list
from gemt.data.util.data_util import generate_key
from controller import KeysHandler
import time

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


def validate_key():
    if 'KEY' in request.headers:
        if request.headers.get('KEY') == '38eedfc994339fbcf3b2025196068d99':
            return
    return abort(403)


@app.route('/', methods=['GET'])
def index():
    return '<br>'.join(help_app)


@app.route('/help', methods=['GET'])
def help_route():
    return jsonify({'Help Message': help_app})


@app.route('/get_all', methods=['GET'])
def get_all_content_view():
    validate_key()
    return jsonify({'All': get_all()})


@app.route('/get_free', methods=['GET'])
def get_free_key_views():
    validate_key()
    return jsonify({'All': get_free_content()})


@app.route('/summary', methods=['GET'])
def get_summary_view():
    validate_key()
    return jsonify({'All': get_summary(), 'free_keys': get_free_keys_list()})


@app.route('/add', methods=['POST'])
def add_key():
    """
    Add a number of keys equals to key_value.
    :return:
    """
    validate_key()
    validate_schema(mandatory=['key_value'])
    added = []
    for _ in range(int(request.json['key_value'])):
        added.append(KeysHandler(generate_key()).add_key())
        time.sleep(1)
    return jsonify({'Result': added})


@app.route('/check/<string:key_value>', methods=['PUT'])
def check_key(key_value):
    validate_schema(mandatory=['machine_id'])
    return jsonify({'Result': KeysHandler(key_value).validate_key(request.json['machine_id'])})


@app.route('/authenticate/<string:key_value>', methods=['PUT'])
def authenticate_key(key_value):
    validate_schema(mandatory=['machine_id'])
    return jsonify({'Result': KeysHandler(key_value).authenticate_key(request.json['machine_id'])})