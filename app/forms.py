from flask_wtf import FlaskForm 
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField, DateTimeField, DateField, SubmitField, FieldList, FormField, TextField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from app.models import Airport, Check_in
import datetime

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

def get_diagTimes(airport_code):
    selection = Check_in.query.filter(Check_in.airport_id==airport_code).all()
    diag_timings = []
    for i in selection:
        diag_timings.append(i.diag_time)
    return (diag_timings)

# def get_diagTimes(airport_code):
#     selection = Check_in.query.filter(Check_in.airport_id==airport_code).all()
#     diag_timings = []
#     count = 0
#     for i in selection:
#         diag_timings.append((count,) + (i.diag_time.strftime('%B %d, %Y'))) # not tuple?
#     return (diag_timings)

class CompareForm(FlaskForm):
    airport_info = Airport.query.all()
    airports = []
    for airport in airport_info:
        if get_diagTimes(airport.iata_code) != []:     # Remove airports without any diagnostics performed
            airports.append([airport, airport.name, get_diagTimes(airport.iata_code)])
    for airport in airports:
        for date in airport[2]:
            # print (str(airport[0])+'_'+date.strftime('%Y-%m-%d'))
            combined = str(airport[1])+'@'+date.strftime('%B %d, %Y')
            setattr(FlaskForm, combined, BooleanField())
    # for airport in airport_info:
    #     print (airport.name,get_diagTimes(airport.iata_code))
    #     setattr(FlaskForm, airport.name, SelectMultipleField(airport.name, choices=[('a', get_diagTimes(airport.iata_code))]))

