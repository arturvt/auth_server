"""
Run GEMT Server
"""
from gemt import app

if __name__ == '__main__':
    # app.logger.info('Starting app...')
    app.run(debug=True)
    # app.run()
