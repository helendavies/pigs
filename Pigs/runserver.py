"""
This script runs the Pigs application using a development server.
"""

from os import environ
from Pigs import app

if __name__ == '__main__':
    
    app.run(port = 8000, debug = True)
