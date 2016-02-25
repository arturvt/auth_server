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


def get_free_content():
    """
    Lists the keys and computer ids.
    :return:
    """
    all_keys = KeyModel.query.all()
    result = [k.get_dict() for k in all_keys if k.authenticated_date is None]
    return result


def get_free_keys_list():
    all_keys = KeyModel.query.all()
    result = [k.reader_key for k in all_keys if k.authenticated_date is None]
    return result


def delete_one_used():
    result = []
    all_keys = KeyModel.query.all()
    for ent in all_keys:
        if ent.authenticated_date is not None:
            result.append(ent.get_dict())
            db_session.delete(ent)
    db_session.commit()
    return result


def get_summary():
    all_keys = KeyModel.query.all()
    total = len(all_keys)
    non_used = [k.get_dict() for k in all_keys if k.authenticated_date is None]
    free_keys = len(non_used)
    return {
        'total_keys': total,
        'used_keys': total - free_keys,
        'free_keys': free_keys
    }


def add_key(reader_key):
    k = KeyModel(reader_key)
    db_session.add(k)
    db_session.commit()
    return k.get_dict()


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
