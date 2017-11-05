"""
This is the routes file for promo
"""
from flask import Blueprint, render_template
from app.promo.models import Packages, HotelBookings, FlightBooking, DB
from app.promo import forms

MOD_PROMO = Blueprint('promo', __name__, template_folder='templates',
                      static_folder='static', static_url_path='/%s' % __name__)


@MOD_PROMO.route('/')
def promos():
    """ Promos """
    packages = Packages.query.order_by(Packages.package_id.desc()).all()
    return render_template("packages.html", packages=packages)


@MOD_PROMO.route('/package/<int:package_id>')
def package():
    """ Package """
    packages = Packages.query.all()
    return render_template('package.html', packages=packages)


@MOD_PROMO.route('/flights', methods=['GET', 'POST'])
def flights():
    """ Flights """
    form = forms.FlightForm()
    # print(form.errors)
    if form.validate_on_submit():
        flight = FlightBooking(fbooking_email=form.email.data, fbooking_departure=form.place_from.data,
                               fbooking_arrival=form.place_to.data, fbooking_departure_date=form.departure_date.data, fbooking_arrival_date=form.arrival_date.data,
                               fbooking_budget_range=form.budget_range.data, fbooking_head_count=form.head_count.data)
        DB.session.add(flight)
        DB.session.commit()
        return '<h1>Flight Destination: ' + form.place_to.data + '</h1> Validate on Submit'
    print(form.errors)
    # if form.is_submitted():
    # return '<h1>Flight Destination:' + form.place_to.data + '</h1> Submitted'
    return render_template("flightbooking.html", form=form)


@MOD_PROMO.route('/bookings', methods=['GET', 'POST'])
def bookings():
    """ Bookings """
    form = forms.HotelForm()
    if form.validate_on_submit():
        hotel = HotelBookings(hbooking_email=form.email.data, hbooking_location=form.hotel_location.data, hbooking_check_in=form.check_in_date.data,
                              hbooking_check_out=form.check_out_date.data, hbooking_number_of_rooms=form.number_of_rooms.data, hbooking_budget_range=form.budget_range.data)
        DB.session.add(hotel)
        DB.session.commit()
        return '<h1>Hotel Bookings: ' + form.hotel_location.data + '</h1>'
    print(form.errors)
    return render_template("hotelbooking.html", form=form)
