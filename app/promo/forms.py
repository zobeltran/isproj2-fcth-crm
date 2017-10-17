"""
Form Class for Promo Modules
"""

from flask_wtf import FlaskForm
from wtforms import validators, StringField, FloatField, IntegerField, SubmitField
from wtforms.fields.html5 import DateField

class FlightForm(FlaskForm):
    """
    Form Class for Flights

    Fields          :   Data Type
    place_from      :   String
    place_to        :   String
    departure_date  :   Date
    arrival_date    :   Date
    budget_range    :   Float
    head_count      :   Integer
    """
    place_from = StringField('Departure Place',
                             validators=[validators.InputRequired(message='Please insert a Departure Place'),
                                         validators.Length(max=100)])
    place_to = StringField('Arrival Place',
                           validators=[validators.InputRequired(message='Please insert an Arrival Place'),
                                       validators.Length(max=100)])
    departure_date = DateField('Departure Date',
                               validators=[validators.InputRequired(message='Please enter a Departure Date')])
    arrival_date = DateField('Arrival Date',
                             validators=[validators.InputRequired(message='Please enter an Arrival Date')])
    budget_range = FloatField('Budget Range',
                              validators=[validators.InputRequired(message='Please enter a Budget Range')])
    head_count = IntegerField('Head Count',
                              validators=[validators.InputRequired(message='Please enter the head count')])
    submit = SubmitField('Submit')

class HotelForm(FlaskForm):
    """
    Form Class for Hotels

    Fields          :   Data Type
    Hotel Location  :   String
    Check in Date   :   Date
    Check out Date  :   Date
    Number of Rooms :   Integer
    Budget Range    :   Float
    """
    hotel_location = StringField('Total Location',
                                 [validators.DataRequired('Please insert a Departure Place'), validators.Length(max=100)],
                                )
    check_in_date = DateField('Departure Date', [validators.DataRequired('Please enter a Departure Date')],
                              format='%m-%d-%Y')
    check_out_date = DateField('Arrival Date', [validators.DataRequired('Please enter an Arrival Date')],
                               format='%m-%d-%y')
    number_of_rooms = IntegerField('Number of Rooms',
                                   [validators.DataRequired('Please Enter number of Rooms needed')])
    budget_range = FloatField('Budget Range',
                              [validators.DataRequired('Please enter a Budget Range')])
