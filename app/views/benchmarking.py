from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required
from app.models import Airport, Check_in, Emigration, Security_checkpoint
from app.forms import CompareForm
import datetime

mod = Blueprint('benchmarking', __name__, url_prefix='/benchmarking')

@mod.route('/')
# @login_required
def index():
    return redirect(url_for('benchmarking.selection'))

# @mod.route('/inside')
# def inside():
#     form = VenueForm()
#     return render_template("benchmarking/benchmarking.html",
#                             form = form,
#                             title = 'Benchmarking')

@mod.route('/selection',methods=['POST','GET'])
@login_required
def selection():
    airport_info = Airport.query.all()
    airports = []
    for airport in airport_info:
        if get_diagTimes(airport.iata_code) != []:     # Remove airports without any diagnostics performed
            airports.append([airport, airport.name , get_diagTimes(airport.iata_code)])

    form = CompareForm()
    # for field in form:
    #     splitted = field.label().split('@')
    #     print (splitted)
    if form.validate_on_submit():
        print(form.data)
        # return redirect(url_for('benchmarking.inside'))
    # else:
        # return redirect(url_for('benchmarking.index'))
    return render_template("benchmarking/selection.html",
                            title = 'Selection',
                            airports = airports,
                            form = form)

@mod.route('/inside',methods=['POST','GET'])
@login_required
def inside():
    form = CompareForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("benchmarking/benchmarking.html", 
                            form=form)

# Get time of diagnosis for a certain airport
def get_diagTimes(airport_code):
    selection = Check_in.query.filter(Check_in.airport_id==airport_code).all()
    diag_timings = []
    for i in selection:
        diag_timings.append(i.diag_time)
    return (diag_timings)
