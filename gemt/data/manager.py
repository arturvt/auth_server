import sqlite3

from util.data_util import generate_key, get_current_date_formated

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


def connect_db():
    return sqlite3.connect('gemt_db.db')


def init_db():
    print 'Init database'
    with connect_db() as db:
        with open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def fill_db():
    db = connect_db()
    c = db.cursor()

    for d in keys_auth.itervalues():
        c.execute('insert into auth_keys (reader_key, machine_id, created_date, authenticated_date) values (?, ?, ?, ?)',
                  [d['reader_key'], d['machine_id'], d['created_date'], d['authenticated_date']])

    for _ in range(20):
        c.execute('insert into auth_keys (reader_key, created_date) values (?, ?)',
                  [generate_key(), get_current_date_formated()])
    db.commit()
    db.close()


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
