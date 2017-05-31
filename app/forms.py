from flask_wtf import FlaskForm 
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField, DateTimeField, DateField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])