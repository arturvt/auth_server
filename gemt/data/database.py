from flask import g
from gemt import app
import sqlite3

COMPLETE_ENTITY_SQL = 'select id, reader_key, machine_id, created_date, authenticated_date from auth_keys'

def connect_db():
    """Connects with database """
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    """ Called before every request """
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    """ Called after response has been constructed """
    db = getattr(g, 'db', None)
    if db is None:
        db.close()


def get_all():
    """
    Lists the keys and computer ids.
    :return:
    """
    cur = g.db.execute('select reader_key, machine_id from auth_keys order by id desc')
    return [dict(reader_key=row[0], machine_id=row[1]) for row in cur.fetchall()]


def list_all_content():
    """
    List all content, including nullable values
    :return:
    """
    cur = g.db.execute(COMPLETE_ENTITY_SQL + ' order by id desc')
    return [dict(id=row[0], reader_key=row[1], machine_id=row[2], created_date=row[3], authenticated_date=row[4]) for row in cur.fetchall()]


def add_key(reader_key, created_date):
    g.db.execute('insert into auth_keys (reader_key, created_date) values (?, ?)',
                 [reader_key, created_date])
    g.db.commit()


def get_key(key_value):
    cur = g.db.execute('select * from auth_keys where reader_key="%s"' % key_value)
    return [dict(id=row[0], reader_key=row[1], machine_id=row[2], created_date=row[3], authenticated_date=row[4]) for row in cur.fetchall()]