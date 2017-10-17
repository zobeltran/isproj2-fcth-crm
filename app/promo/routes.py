"""
This is the routes file for promo
"""
from flask import Blueprint, render_template
from app.promo.models import Packages, HotelBookings, FlightBooking
from app.promo import forms
MOD_PROMO = Blueprint('promo', __name__, template_folder='templates',
                      static_folder='static', static_url_path='/%s' %__name__)

@MOD_PROMO.route('/')
def promos():
    """
    Promos
    """
    packages = Packages.query.order_by(Packages.package_id.desc()).all()
    return render_template("packages.html", packages=packages)

@MOD_PROMO.route('/package/<int:package_id>')
def package():
    """
    Package
    """
    packages = Packages.query.all()
    return render_template('package.html', packages=packages)

@MOD_PROMO.route('/flights', methods=['GET','POST'])
def flights():
    """
    Flights
    """
    form = forms.FlightForm()
    # print(form.errors)
    if form.validate_on_submit():
        return '<h1>Flight Destination: ' + form.place_to.data + '</h1> Validate on Submit'
    print(form.errors)
    # if form.is_submitted():
        # return '<h1>Flight Destination:' + form.place_to.data + '</h1> Submitted'
    return render_template("flightbooking.html", form=form)
