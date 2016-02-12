from gemt.data.util.data_util import get_current_date_formated
from gemt import app, db
from gemt.data.models.key_model import KeyModel

db_session = db.session


@app.teardown_request
def teardown_request(exception):
    """ Called after response has been constructed """
    db_session.remove()


def get_all():
    """
    Lists the keys and computer ids.
    :return:
    """
    all_keys = KeyModel.query.all()
    result = [l.get_dict() for l in all_keys]
    return result


def add_key(reader_key):
    k = KeyModel(reader_key)
    db_session.add(k)
    db_session.commit()


def get_key(key_value):
    result = KeyModel.query.filter_by(reader_key=key_value).first()
    if result is None:
        return None
    return result.get_dict()


def authenticate_key(entity_id, machine_id):
    print entity_id, machine_id
    result = KeyModel.query.filter_by(id=entity_id).first()
    result.machine_id = machine_id
    result.authenticated_date = get_current_date_formated()
    db_session.add(result)
    db_session.commit()
    return 'ok'