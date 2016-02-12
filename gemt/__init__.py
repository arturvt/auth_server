"""
GEMT Authentication server.
This project was developed following Flask pattern of package using that can be found at:
http://flask.pocoo.org/docs/0.10/patterns/packages/
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import gemt.settings

app = Flask(__name__)
app.config.from_object(settings)
if not app.debug:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://atenorio@/postgres'
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://noyexuysxftuxp:fYDvex9Teuv7b2gnjCWCAzQABN@ec2-54-225-215-233.compute-1.amazonaws.com:5432/d9b57eeutg2i1t'
db = SQLAlchemy(app)
db.create_all()


import gemt.views
