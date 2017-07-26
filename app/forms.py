from flask_wtf import FlaskForm 
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField, DateTimeField, DateField, SubmitField, FieldList, FormField, TextField, FloatField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo, NumberRange
from app.models import Airport, Check_in
import datetime

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class EditWeights(FlaskForm):
    checkin_weight = IntegerField('Checkin_weight', [NumberRange(min=0)])
    checkin_p_overdesign = FloatField('Checkin_p_overdesign', [NumberRange(min=0)])
    checkin_p_optimum = FloatField('Checkin_p_optimum', [NumberRange(min=0)])
    checkin_p_suboptimum = FloatField('Checkin_p_suboptimum', [NumberRange(min=0)])
    emigration_weight = IntegerField('Emigration_weight', [NumberRange(min=0)])
    emigration_p_overdesign = FloatField('Emigration_p_overdesign', [NumberRange(min=0)])
    emigration_p_optimum = FloatField('Emigration_p_optimum', [NumberRange(min=0)])
    emigration_p_suboptimum = FloatField('Emigration_p_suboptimum', [NumberRange(min=0)])
    security_weight = IntegerField('Security_weight', [NumberRange(min=0)])
    security_p_overdesign = FloatField('Security_p_overdesign', [NumberRange(min=0)])
    security_p_optimum = FloatField('Security_p_optimum', [NumberRange(min=0)])
    security_p_suboptimum = FloatField('Security_p_suboptimum', [NumberRange(min=0)])
    space_checkin_weight = IntegerField('space_Checkin_weight', [NumberRange(min=0)])
    space_checkin_p_overdesign = FloatField('space_Checkin_p_overdesign', [NumberRange(min=0)])
    space_checkin_p_optimum = FloatField('space_Checkin_p_optimum', [NumberRange(min=0)])
    space_checkin_p_suboptimum = FloatField('space_Checkin_p_suboptimum', [NumberRange(min=0)])
    space_emigration_weight = IntegerField('space_Emigration_weight', [NumberRange(min=0)])
    space_emigration_p_overdesign = FloatField('space_Emigration_p_overdesign', [NumberRange(min=0)])
    space_emigration_p_optimum = FloatField('space_Emigration_p_optimum', [NumberRange(min=0)])
    space_emigration_p_suboptimum = FloatField('space_Emigration_p_suboptimum', [NumberRange(min=0)])
    space_security_weight = IntegerField('space_Security_weight', [NumberRange(min=0)])
    space_security_p_overdesign = FloatField('space_Security_p_overdesign', [NumberRange(min=0)])
    space_security_p_optimum = FloatField('space_Security_p_optimum', [NumberRange(min=0)])
    space_security_p_suboptimum = FloatField('space_Security_p_suboptimum', [NumberRange(min=0)])

class AddArea(FlaskForm):
    checkin_length = FloatField('checkin_length', [NumberRange(min=0)])
    checkin_breadth = FloatField('checkin_breadth', [NumberRange(min=0)])
    emigration_length = FloatField('emigration_length', [NumberRange(min=0)])
    emigration_breadth = FloatField('emigration_breadth', [NumberRange(min=0)])
    security_length = FloatField('security_length', [NumberRange(min=0)])
    security_breadth = FloatField('security_breadth', [NumberRange(min=0)])

class AddAirport(FlaskForm):
    new_iata_code = StringField('new_iata_code', validators=[DataRequired(), Length(min=3,max=3)])
    new_icao_code = StringField('new_icao_code', validators=[DataRequired(), Length(min=4,max=4)])
    new_name = StringField('new_name', validators=[DataRequired()])
    new_city = StringField('new_city', validators=[DataRequired()])
    new_country = StringField('new_country', validators=[DataRequired()])
    new_size = StringField('new_country', validators=[DataRequired()])
