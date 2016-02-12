"""
Run GEMT Server
"""
import os
from gemt import app

# app.run(debug=True)
if __name__ == '__main__':
    print '---- Starting app -----'
    if 'DATABASE_URL' in os.environ:
        app.logger.info(os.environ["DATABASE_URL"])
    # app.run(debug=True)
    app.run()
