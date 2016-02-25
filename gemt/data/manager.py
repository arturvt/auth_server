import sqlite3

from util.data_util import generate_key, get_current_date_formated
from gemt.data.models.key_model import KeyModel
from gemt.data.database import db_session, init_db

keys_auth = {
    "AA": {
        'reader_key': generate_key(),
        'machine_id': 'BA110544d821 ',
        'created_date': '2016/02/12 - 01:30:00',
        'authenticated_date': '2016/02/16 - 01:30:00'
    },
    "A": {
        'reader_key': generate_key(),
        'machine_id': 'DE110544d821 ',
        'created_date': '2016/02/12 - 01:31:00',
        'authenticated_date': '2016/02/16 - 01:31:00'
    }
}


def fill_db():
    for _ in range(20):
        k = KeyModel(generate_key())
        db_session.add(k)

    db_session.commit()
    db_session.close()


def get_keys():
    db = connect_db()
    cur = db.execute('select reader_key, machine_id from auth_keys order by id desc')
    return [dict(reader_key=row[0], machine_id=row[1]) for row in cur.fetchall()]

if __name__ == '__main__':
    print 'Starting'
    init_db()
    fill_db()
    print 'Reading contents:'
    print get_keys()
    print 'Finish'
