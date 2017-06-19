from flask import Blueprint, render_template, redirect, flash, url_for
# from flaskext.mysql import MySQL
from app import app
from flask_login import login_required
from app.models import Airport, Check_in, Emigration, Security_checkpoint
import datetime
import random

mod = Blueprint('diagnostics', __name__, url_prefix='/diagnostics')

@mod.route('/')
@login_required
def index():
    return redirect(url_for('diagnostics.selection'))

@mod.route('/selection',methods=['POST','GET'])
@login_required
def selection():
    airport_info = Airport.query.all()
    airports = []
    for airport in airport_info:
        if get_diagTimes(airport) != []:     # Remove airports without any diagnostics performed
            airports.append([airport, airport.name , get_diagTimes(airport)])
    # print (airports)
    return render_template("diagnostics/selection.html",
                            title = 'Selection',
                            airports = airports)

# @mod.route('/<airport_code>/')
# @login_required
# def diagnostics(airport_code):
#     return redirect(url_for('diagnostics.selection'))

@mod.route('/<airport_code>/<diag_time>')
@login_required
def diagnostics(airport_code, diag_time):
    current_Time = datetime.datetime.strptime(diag_time, "%Y-%m-%d")
    # print (type(current_Time))
    checkin_info = Check_in.query.get((airport_code, diag_time))
    emigration_info = Emigration.query.get((airport_code, diag_time))
    security_info = Security_checkpoint.query.get((airport_code, diag_time))
    return render_template("diagnostics/diagnostics.html", 
                            title = "Diagnostics for "+ airport_code, 
                            airport_info = Airport.query.get(airport_code),
                            diagTime = get_diagTimes(airport_code),
                            current_Time = current_Time,
                            checkin_info = checkin_info,
                            emigration_info = emigration_info,
                            security_info = security_info,
                            score = random.randrange(70, 95))

# Get time of diagnosis for a certain airport
def get_diagTimes(airport_code):
    selection = Check_in.query.filter(Check_in.airport_id==airport_code).all()
    diag_timings = []
    for i in selection:
        diag_timings.append(i.diag_time)
    return (diag_timings)