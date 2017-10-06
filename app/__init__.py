"""
The init file of the main application
"""
from flask import Flask
from app.promo.routes import MOD_PROMO

APP = Flask(__name__, static_folder=None)

APP.register_blueprint(MOD_PROMO)

if __name__ == '__main__':
    APP.run()
