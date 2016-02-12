from gemt.data.util.data_util import get_current_date_formated
from gemt import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


COMPLETE_ENTITY_SQL = 'select id, reader_key, machine_id, created_date, authenticated_date from auth_keys'

engine = create_engine('postgresql+psycopg2://atenorio@/postgres', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

from gemt.data.models.key_model import KeyModel


def init_db():
    import gemt.data.models.key_model
    Base.metadata.create_all(bind=engine)


# @app.before_request
# def before_request():
#     """ Called before every request """
#     g.db = db


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