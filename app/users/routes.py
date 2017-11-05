"""
This is the User Routes
"""
from flask import Blueprint, render_template
from app.users.models import User

MOD_USER = Blueprint('user', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/%s' % __name__)


@MOD_USER.route('/user')
def login():
    """ This is the login route """
    return render_template("login.html")
