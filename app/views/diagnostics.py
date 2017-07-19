from flask import Blueprint, render_template, redirect, flash, url_for
# from flaskext.mysql import MySQL
from app import app
from flask_login import login_required
from app.models import Airport, Check_in, Emigration, Security_checkpoint, Iata_los, Metric
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
        if get_diagTimes(airport.iata_code) != []:     # Remove airports without any diagnostics performed
            airports.append([airport, airport.name , get_diagTimes(airport.iata_code)])
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
    # Get IATA LoS grades of each value
    checkin_grade = get_grade('check_in',checkin_info.sys_waitingtime)
    emigration_grade = get_grade('emigration',emigration_info.sys_waitingtime)
    security_grade = get_grade('security_checkpoint',security_info.sys_waitingtime)
    score = overall_grade(checkin_grade,emigration_grade,security_grade)
    return render_template("diagnostics/diagnostics.html", 
                            title = "Diagnostics for "+ airport_code, 
                            airport_info = Airport.query.get(airport_code),
                            diagTime = get_diagTimes(airport_code),
                            current_Time = current_Time,
                            checkin_info = checkin_info,
                            emigration_info = emigration_info,
                            security_info = security_info,
                            checkin_grade = checkin_grade,
                            emigration_grade = emigration_grade,
                            security_grade = security_grade,
                            score = score)

# Get time of diagnosis for a certain airport
def get_diagTimes(airport_code):
    selection = Check_in.query.filter(Check_in.airport_id==airport_code).all()
    diag_timings = []
    for i in selection:
        diag_timings.append(i.diag_time)
    return (diag_timings)

def get_grade(process,value):
    proc_OD_UB = Iata_los.query.get(process).overdesign_UB
    proc_SO_LB = Iata_los.query.get(process).suboptimum_LB
    if value/60 < proc_OD_UB:  #value is in seconds
        result = 'Over-design'
    elif value > proc_SO_LB:
        result = 'Suboptimum'
    else:
        result = 'Optimum'
    return result

def overall_grade(checkin_grade, emigration_grade, security_grade):
    score = 1/3*(process_point("check_in",checkin_grade)+process_point("emigration",emigration_grade)+process_point("security_checkpoint",security_grade))
    print (score)
    if score >2:
        grade = "A"
    elif score<=2 and score>1:
        grade = "B"
    elif score<=1:
        grade = "C"
    return grade

def process_point(process,grade):
    metrics = Metric.query.get(process)
    weight = metrics.weight
    if grade == "Over-design":
        points = metrics.p_overdesign
    elif grade == "Optimum":
        points = metrics.p_optimum
    elif grade == "Suboptimum":
        points = metrics.p_suboptimum
    return weight*points

