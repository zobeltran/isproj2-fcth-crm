"""
The init file of the main application
"""
from flask import Flask

APP = Flask(__name__, static_folder=None)

if __name__ == '__main__':
    APP.run()
