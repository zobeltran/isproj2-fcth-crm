"""
Form Class for Promo Modules
"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length, Email
from wtforms.fields.html5 import DateField


class FlightForm(FlaskForm):
    """
    Form Class for Flights

    Fields          :   Data Type
    email           :   Email
    place_from      :   String
    place_to        :   String
    departure_date  :   Date
    arrival_date    :   Date
    budget_range    :   Float
    head_count      :   Integer
    """

    email = StringField('Email Address',
                        validators=[InputRequired(message='Please insert an Email Address'),
                                    Email(
                                        message='Please input a valid Email Address'),
                                    Length(max=100)])
    place_from = StringField('Departure Place',
                             validators=[InputRequired(message='Please insert a Departure Place'),
                                         Length(max=100)])
    place_to = StringField('Arrival Place',
                           validators=[InputRequired(message='Please insert an Arrival Place'),
                                       Length(max=100)])
    departure_date = DateField('Departure Date',
                               validators=[InputRequired(message='Please enter a Departure Date')])
    arrival_date = DateField('Arrival Date',
                             validators=[InputRequired(message='Please enter an Arrival Date')])
    budget_range = FloatField('Budget Range',
                              validators=[InputRequired(message='Please enter a Budget Range')])
    head_count = IntegerField('Head Count',
                              validators=[InputRequired(message='Please enter the head count')])
    submit = SubmitField('Submit')


class HotelForm(FlaskForm):
    """
    Form Class for Hotels.

    Email           =   Email
    Hotel Location  =   String
    Check in Date   =   Date
    Check out Date  =   Date
    Number of Rooms =   Integer
    Budget Range    =   Float
    """
    email = StringField('Email Address',
                        validators=[DataRequired('Please insert an Email Address'),
                                    Email(
                                        message='Please insert a valid Email Address'),
                                    Length(max=100)])
    hotel_location = StringField('Hotel Location',
                                 [DataRequired('Please insert a Departure Place'),
                                  Length(max=100)])
    check_in_date = DateField('Departure Date',
                              [DataRequired('Please enter a Departure Date')])
    check_out_date = DateField('Arrival Date',
                               [DataRequired('Please enter an Arrival Date')])
    number_of_rooms = IntegerField('Number of Rooms',
                                   [DataRequired('Please Enter number of Rooms needed')])
    budget_range = FloatField('Budget Range',
                              [DataRequired('Please enter a Budget Range')])
    submit = SubmitField('Submit')
