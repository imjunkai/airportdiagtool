from flask import Blueprint, render_template, redirect, flash, url_for
from flaskext.mysql import MySQL
from app import app
from flask_login import login_required
from app.models import Airport, Check_in

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'adt'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

mod = Blueprint('diagnostics', __name__, url_prefix='/diagnostics')

@mod.route('/')
@login_required
def index():
    return redirect(url_for('diagnostics.selection'))

@mod.route('/selection',methods=['POST','GET'])
@login_required
def selection():
    return render_template("diagnostics/selection.html",
                            title = 'Selection',
                            airports = Airport.query.all())

@mod.route('/<airport_code>/')
@login_required
def diagnostics(airport_code):
    return render_template("diagnostics/diagnostics.html",
                            title = "Diagnostics for "+ airport_code,
                            airport_info = Airport.query.get(airport_code))

# @mod.route('/<airport_code>/<diag_time>')
# @login_required
# def diagnostics(airport_code, diag_time):
# 	diag_timings = Check_in.query.filter(Check_in.airport_id == airport_code)
	
# 	if diag_time is None:
# 		print('ha')
# 		pass
#     return render_template("diagnostics/diagnostics.html", 
#                             title = "Diagnostics for "+ airport_code, 
#                             airport_info = Airport.query.get(airport_code))