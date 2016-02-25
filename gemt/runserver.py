"""
Run GEMT Server
"""
from gemt import app

# app.run(debug=True)
if __name__ == '__main__':
    print '=== Starting from local ==='
    app.run(debug=True)
