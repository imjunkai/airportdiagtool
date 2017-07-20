from flask import Blueprint, render_template, redirect, flash, url_for, request, Flask
from flask_login import login_required
from app.models import Airport, Check_in, Emigration, Security_checkpoint
from app.forms import CompareForm
import datetime
from collections import OrderedDict

mod = Blueprint('benchmarking', __name__, url_prefix='/benchmarking')

@mod.route('/')
@login_required
def index():
    return redirect(url_for('benchmarking.selection'))

@mod.route('/selection',methods=['POST','GET'])
@login_required
def selection():
    airport_info = Airport.query.all()
    airports = []
    for airport in airport_info:
        if get_diagTimes(airport.iata_code) != []:     # Remove airports without any diagnostics performed
            airports.append([airport, airport.name , get_diagTimes(airport.iata_code)])
    return render_template("benchmarking/selection.html",
                            title = 'Selection',
                            airports = airports)

@mod.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    result = dict(request.form)
    airports = []
    for key, value in result.items():
        airports.append([key,value])
    print (airports)
    airports_info = {}
    for i in range(0,len(airports)):   # Iterate through all airports
        for j in range(0,len(airports[i][1])):    # Iterate through all diagnostic timings of current airport
            print (airports[i][1][j])
            key = airports[i][0]+ '_'+airports[i][1][j]
            airports_info[key] = {}
            airports_info[key]['iata_code'] = airports[i][0]
            airports_info[key]['diag_time'] = datetime.datetime.strptime(airports[i][1][j], '%Y-%m-%d')
            airports_info[key]['information'] = Airport.query.get(airports[i][0])
            airports_info[key]['checkin'] = Check_in.query.get((airports[i][0], airports[i][1][j]))
            airports_info[key]['emigration'] = Emigration.query.get((airports[i][0], airports[i][1][j]))
            airports_info[key]['security'] = Security_checkpoint.query.get((airports[i][0], airports[i][1][j]))

    return render_template("benchmarking/result.html",
                            airports_info = airports_info,
                            title = 'Benchmarking')

# Get time of diagnosis for a certain airport
def get_diagTimes(airport_code):
    selection = Check_in.query.filter(Check_in.airport_id==airport_code).all()
    diag_timings = []
    for i in selection:
        diag_timings.append(i.diag_time)
    return (diag_timings)
