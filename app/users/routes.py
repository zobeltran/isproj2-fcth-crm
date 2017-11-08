"""
This is the User Routes
"""
from flask import Blueprint, render_template
from app.models import Packages, HotelBookings, FlightBooking, DB
from flask_user import login_required
from datetime import datetime
from app.users import forms
from app.models import Packages

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


@MOD_USER.route('/user/createpromo', methods=['POST', 'GET'])
@login_required
def promo():
    """ Promo Creation page """
    form = forms.PackagesForm()
    if form.validate_on_submit():
        package = Packages(package_name=form.package_name.data, package_description=form.description.data,
                           package_price=form.package_price.data, package_createtime=datetime.today(), package_updated=datetime.today())
        DB.session.add(package)
        DB.session.commit()
        return render_template("homepage.html")
    print(form.errors)
    return render_template('createpackage.html', form=form)
