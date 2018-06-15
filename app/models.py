"""
This is the User's Model
"""
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin
from flask_migrate import Migrate

DB = SQLAlchemy()
MIGRATE = Migrate()


# User Model
class User(DB.Model, UserMixin):
    """
    User Model
    """
    id = DB.Column('Id', DB.Integer, primary_key=True)

    # User Authentication information
    username = DB.Column('Username', DB.String(50), unique=True)
    password = DB.Column('Password', DB.String(255))

    # User Email information
    email = DB.Column('EmailAddress', DB.String(255), unique=True)
    confirmed_at = DB.Column('ConfirmedAt', DB.DateTime())

    # User information
    is_enabled = DB.Column('IsEnabled', DB.Boolean(), default=False)
    first_name = DB.Column('FirstName', DB.String(50))
    last_name = DB.Column('LastName', DB.String(50))

    # Relationships
    roles = DB.relationship('Role', secondary='UserRoles')

    __tablename__ = 'Users'

    def is_active(self):
        return self.is_enabled


# Roles Model
class Role(DB.Model):
    """
    Roles Model
    """
    id = DB.Column('Id', DB.Integer, primary_key=True)
    name = DB.Column('Name', DB.String(100))
    __tablename__ = 'Roles'


# User Roles Model
class UserRoles(DB.Model):
    """
    User Roles Assignment Model
    """
    id = DB.Column('Id', DB.Integer, primary_key=True)
    user_id = DB.Column('UserId', DB.Integer, DB.ForeignKey('Users.Id',
                        ondelete='CASCADE'))
    role_id = DB.Column('RoleId', DB.Integer, DB.ForeignKey('Roles.Id',
                        ondelete='CASCADE'))
    __tablename__ = 'UserRoles'


# Promo model
class Packages(DB.Model):
    """
    Package Model
    """
    id = DB.Column('Id', DB.Integer, primary_key=True)
    packageName = DB.Column('Name', DB.String(100))
    packageDescription = DB.Column('Description', DB.String(200))
    packagePrice = DB.Column('Price', DB.Integer)
    packageCreateTime = DB.Column('CreatedTime', DB.DateTime)
    packageUpdated = DB.Column('UpdatedTime', DB.DateTime)
    __tablename__ = 'Package'

    def __repr__(self):
        return '<Package(PackageName = %r)>' % self.package_name


class HotelBookings(DB.Model):
    """
    Hotel Bookings Model
    """
    hbooking_id = DB.Column('Id', DB.Integer, primary_key=True)
    hbooking_email = DB.Column('Email', DB.String(100))
    hbooking_location = DB.Column('Location', DB.String(200))
    hbooking_check_in = DB.Column('CheckIn', DB.Date)
    hbooking_check_out = DB.Column('CheckOut', DB.Date)
    hbooking_number_of_rooms = DB.Column('NumberOfRoom', DB.Integer)
    hbooking_budget_range = DB.Column('BudgetRange', DB.Integer)
    __tablename__ = 'HotelBookingRequest'

    def __repr__(self):
        return '<Hotel (HotelName = %r)>' % self.hbooking_name


class FlightBooking(DB.Model):
    """
    Flight Bookings Model
    """
    fbooking_id = DB.Column('Id', DB.Integer, primary_key=True)
    fbooking_email = DB.Column('Email', DB.String(100))
    fbooking_departure = DB.Column('Departure', DB.String(100))
    fbooking_arrival = DB.Column('Arrival', DB.String(200))
    fbooking_departure_date = DB.Column('DepartureDate', DB.Date)
    fbooking_arrival_date = DB.Column('ArrivalDate', DB.Date)
    fbooking_budget_range = DB.Column('BudgetRange', DB.Integer)
    fbooking_head_count = DB.Column('HeadCount', DB.Integer)
    __tablename__ = 'FlightBookingRequest'

    def __repr__(self):
        return '<Flight (%r - %r)>' % self.fbooking_departure,
        self.fbooking_arrival


class Customer(DB.Model):
    """
    Customer Model
    """
    id = DB.Column('Id', DB.Integer, primary_key=True)
    customerTitle = DB.Column('Title', DB.String(5))
    customerFirstName = DB.Column('FirstName', DB.String(50))
    customerMiddleName = DB.Column('MiddleName', DB.String(50))
    customerLastName = DB.Column('LastName', DB.String(50))
    customerEmail = DB.Column('EmailAddress', DB.String(150))
    customerContactNo = DB.Column('ContactNo', DB.Integer)
    customerBirthday = DB.Column('Birthday', DB.Date)
    customerNationality = DB.Column('Nationality', DB.String(50))
    customerGender = DB.Column('Gender', DB.String(6))
    __tablename__ = 'Customer'

    def __repr__(self):
        return '<Customer (FullName = %r %r)>' % self.customerFirstName,
        self.customerLastName
