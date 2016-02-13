"""
GEMT Authentication server.
This project was developed following Flask pattern of package using that can be found at:
http://flask.pocoo.org/docs/0.10/patterns/packages/
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import gemt.settings
import os

app = Flask(__name__)
app.config.from_object(settings)
if not os.environ.has_key('DATABASE_URL'):
    os.environ['DATABASE_URL'] = 'postgresql+psycopg2://atenorio@/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]

db = SQLAlchemy(app)
db.create_all()


import gemt.views
