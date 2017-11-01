"""
This is the run file
"""
from app import APP

if __name__ == '__main__':
    APP.jinja_env.cache = {}
    APP.run()
