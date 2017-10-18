"""
Models for Promos Module
"""
from flask_sqlalchemy import SQLAlchemy

# Database Initialization
DB = SQLAlchemy()

class Packages(DB.Model):
    """
    Package Model
    """
    package_id = DB.Column(DB.Integer, primary_key=True)
    package_name = DB.Column(DB.String(100), nullable=False)
    package_description = DB.Column(DB.String(200), nullable=False)
    package_price = DB.Column(DB.Float)
    package_createtime = DB.Column(DB.DateTime)
    package_updated = DB.Column(DB.DateTime)
    __tablename__ = 'Package'

    def __repr__(self):
        return '<Package %r)' % self.package_name

class HotelBookings(DB.Model):
    """
    Hotel Bookings Model
    """
    hbooking_id = DB.Column(DB.Integer, primary_key=True)
    hbooking_location = DB.Column(DB.String(200), nullable=False)
    hbooking_check_in = DB.Column(DB.String(50))
    hbooking_check_out = DB.Column(DB.String(50))
    hbooking_number_of_rooms = DB.Column(DB.Integer)
    hbooking_budget_range = DB.Column(DB.Float)
    __tablename__ = 'Hotel_Booking_Request'

    def __repr__(self):
        return '<Hotel %r)' % self.hbooking_name

class FlightBooking(DB.Model):
    """
    Flight Bookings Model
    """
    fbooking_id = DB.Column(DB.Integer, primary_key=True)
    fbooking_departure = DB.Column(DB.String(100), nullable=False)
    fbooking_arrival = DB.Column(DB.String(200), nullable=False)
    fbooking_departure_date = DB.Column(DB.String(50), nullable=False)
    fbooking_arrival_date = DB.Column(DB.String(50), nullable=False)
    fbooking_budget_range = DB.Column(DB.Float)
    fbooking_head_count = DB.Column(DB.Integer)
    fbooking__tablename__ = 'Flight_Booking_Request'

    def __repr__(self):
        return '<Flight %r - %r)' % self.fbooking_departure, self.fbooking_arrival
