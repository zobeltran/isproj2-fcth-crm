"""
The init file of the main application
NOTE: __init__.py is a special Python file that allows a directory to become
a Python package so it can be accessed using the 'import' statement
"""
from flask import Flask
from flask_user import UserManager
# CSRF
from flask_wtf.csrf import CSRFProtect
# Models
from app.promo.models import DB as DBPROMO, MIGRATE as MIGRATEPROMO
from app.users.models import DB as DBUSER, MIGRATE as MIGRATEUSER
# Routes
from app.promo.routes import MOD_PROMO
from app.users.routes import MOD_USER
# from app.users.models import DB as DBUSER
# Models DB Adaptor
# from app.users.models import DB_ADAPTER
# Flask Migrations
from flask_migrate import Migrate, MigrateCommand


# Flask Initialization
APP = Flask(__name__, static_folder=None)

# Database Initialization
DBPROMO.init_app(APP)
DBUSER.init_app(APP)

# CSRF Protection
CSRF = CSRFProtect(APP)

# Flask User Initialization
# USER_MANAGER = UserManager(DB_ADAPTER, APP)

# Flask Migrations Initialization
MIGRATEPROMO.init_app(APP, DBPROMO)
MIGRATEUSER.init_app(APP, DBPROMO)

# Configuration
APP.config.from_object('config.ProductionConfig')

# Blueprint Registration
APP.register_blueprint(MOD_PROMO)
APP.register_blueprint(MOD_USER)

if __name__ == '__main__':
    APP.jinja_env.cache = {}
    APP.run()
