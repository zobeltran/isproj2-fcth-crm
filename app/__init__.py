"""
The init file of the main application
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.promo.routes import MOD_PROMO

# Flask Initialization
APP = Flask(__name__, static_folder=None)
# Database Initialization
DB = SQLAlchemy(APP)
APP.register_blueprint(MOD_PROMO)


APP.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    APP.jinja_env.cache = {}
    APP.run()
