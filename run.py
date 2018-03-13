"""
This is the run file
"""
from app import APP
from app import SOCKETIO

if __name__ == '__main__':
    APP.jinja_env.cache = {}
    SOCKETIO.run(APP)
