"""
Models for Promos Module
"""
from app import DB

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
    hbooking_name = DB.Column(DB.String(100), nullable=False)
    hbooking_description = DB.Column(DB.String(200), nullable=False)
    hbooking_price = DB.Column(DB.Float)
    hbooking_createtime = DB.Column(DB.DateTime)
    hbooking_updated = DB.Column(DB.DateTime)
    __tablename__ = 'Hotel_Bookings'
    def __repr__(self):
        return '<Hotel %r)' % self.hbooking_name

class FlightBooking(DB.Model):
    """
    Flight Bookings Model
    """
    fbooking_id = DB.Column(DB.Integer, primary_key=True)
    fbooking_name = DB.Column(DB.String(100), nullable=False)
    fbooking_description = DB.Column(DB.String(200), nullable=False)
    fbooking_price = DB.Column(DB.Float)
    fbooking_createtime = DB.Column(DB.DateTime)
    fbooking_updated = DB.Column(DB.DateTime)
    fbooking__tablename__ = 'Flight_Bookings'
    def __repr__(self):
        return '<Flight %r)' % self.fbooking_name
