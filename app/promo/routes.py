"""
This is the routes file for promo
"""
from flask import Blueprint, render_template

MOD_PROMO = Blueprint('promo', __name__, template_folder='templates',
                      static_folder='static', static_url_path='/%s' %__name__)

@MOD_PROMO.route('/')
def promos():
    """
    Promos
    """
    return render_template("packages.html")
