"""
GEMT Authentication server.
This project was developed following Flask pattern of package using that can be found at:
http://flask.pocoo.org/docs/0.10/patterns/packages/
"""

from flask import Flask
import gemt.settings

app = Flask(__name__)
app.config.from_object(settings)

import gemt.views
