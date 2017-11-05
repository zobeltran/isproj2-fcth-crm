"""
This is the User's Model
"""
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin, SQLAlchemyAdapter, UserManager
from flask_migrate import Migrate

DB = SQLAlchemy()
MIGRATE = Migrate()

# User Model


class User(DB.Model, UserMixin):
    """
    User Model
    """
    id = DB.Column('User_id', DB.Integer, primary_key=True)

    # User email information
    email = DB.Column('User_email', DB.String(255),
                      nullable=False, unique=True)
    confirmed_at = DB.Column('User_confirmed', DB.DateTime())

    # User information
    is_enabled = DB.Column(DB.Boolean(), nullable=False, default=False)
    first_name = DB.Column('User_First_Name', DB.String(50), nullable=False)
    last_name = DB.Column('User_Last_Name', DB.String(50), nullable=False)
    active = DB.Column('User_active', DB.Boolean())
    # Relationships
    user = DB.relationship('UserAuth', backref='userauth', lazy=True)


class UserAuth(DB.Model, UserMixin):
    """
    User Authentication
    """
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer(), DB.ForeignKey(
        'user.User_id', ondelete='CASCADE'))

    # User authentication information
    username = DB.Column(DB.String(50), nullable=False, unique=True)
    password = DB.Column(DB.String(255), nullable=False)


# Flask-User Initialization
DB_ADAPTER = SQLAlchemyAdapter(DB, User, UserAuthClass=UserAuth)

# Promo model


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
    hbooking_email = DB.Column(DB.String(100))
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
    fbooking_email = DB.Column(DB.String(100))
    fbooking_departure = DB.Column(DB.String(100), nullable=False)
    fbooking_arrival = DB.Column(DB.String(200), nullable=False)
    fbooking_departure_date = DB.Column(DB.Date, nullable=False)
    fbooking_arrival_date = DB.Column(DB.Date, nullable=False)
    fbooking_budget_range = DB.Column(DB.Float)
    fbooking_head_count = DB.Column(DB.Integer)
    __tablename__ = 'Flight_Booking_Request'

    def __repr__(self):
        return '<Flight %r - %r)' % self.fbooking_departure, self.fbooking_arrival
