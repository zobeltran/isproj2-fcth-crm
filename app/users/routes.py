"""
This is the User Routes
"""
from flask import Blueprint, render_template
from app.models import Packages, HotelBookings, FlightBooking, DB
from flask_user import login_required

MOD_USER = Blueprint('main', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/%s' % __name__)


@MOD_USER.route('/user')
@login_required
def homepage():
    """ User Homepage """
    flights = FlightBooking.query.order_by(
        FlightBooking.fbooking_id.desc()).all()
    hotels = HotelBookings.query.order_by(
        HotelBookings.hbooking_id.desc()).all()
    return render_template("homepage.html", flights=flights, hotels=hotels)
