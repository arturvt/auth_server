from sqlalchemy import Column, Integer, String
from gemt.data.util.data_util import get_current_date_formated
from gemt import db


class KeyModel(db.Model):

    __tablename__ = 'auth_keys'

    id = Column(Integer, primary_key=True)
    reader_key = Column(String(50), nullable=False)
    machine_id = Column(String(50), nullable=True)
    created_date = Column(String(25), nullable=False)
    authenticated_date = Column(String(25), nullable=True)

    def __init__(self, reader_key):
        self.reader_key = reader_key
        self.created_date = get_current_date_formated()

    def __repr__(self):
        return '<Key %r / MachineId %r>' % (self.reader_key, self.machine_id)

    def get_dict(self):
        return dict(id=self.id, reader_key=self.reader_key, machine_id=self.machine_id,
                    created_date=self.created_date, authenticated_date=self.authenticated_date)
