from flask import Blueprint, render_template, redirect, flash, url_for, request
from app import app, db
from flask_login import login_required
from app.models import Airport, Check_in, Emigration, Security_checkpoint, Iata_los, Metric
from app.forms import AddArea, AddAirport, AddDiagnostics, AddDiagnostics_Simple
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

@mod.route('/addairport',methods=['POST','GET'])
@login_required
def addairport():
    form = AddAirport()
    if request.method == 'POST' and form.validate():
        newAirport = Airport(
            iata_code = form.new_iata_code.data,
            icao_code = form.new_icao_code.data,
            name = form.new_name.data,
            city = form.new_city.data,
            country = form.new_country.data,
            size = form.new_size.data)
        # print (newAirport)
        db.session.add(newAirport)
        db.session.commit()
        return redirect(url_for('diagnostics.selection'))
    return render_template("diagnostics/addairport.html",
                            title = 'Add Airport',
                            form = form)

@mod.route('/adddiagnostics',methods=['POST','GET'])
@login_required
def adddiagnostics():
    form = AddDiagnostics()
    if request.method == 'POST' and form.validate():
        newCheckin = Check_in(
            airport_id = form.iata_code.data,
            diag_time = form.diag_time.data,
            uti_rate = form.checkin_uti_rate.data,
            queue_avgpeople = form.checkin_queue_avgpeople.data,
            queue_waitingtime = form.checkin_queue_waitingtime.data,
            sys_avgpeople = form.checkin_sys_avgpeople.data,
            sys_waitingtime = form.checkin_sys_waitingtime.data,
            avgwaitingarea_space = round(form.checkin_waitingarea_length.data*form.checkin_waitingarea_breadth.data/form.checkin_queue_avgpeople.data,1),
            waitingarea_length = form.checkin_waitingarea_length.data,
            waitingarea_breadth = form.checkin_waitingarea_breadth.data)
        
        newEmigration = Emigration(
            airport_id = form.iata_code.data,
            diag_time = form.diag_time.data,
            uti_rate = form.emigration_uti_rate.data,
            queue_avgpeople = form.emigration_queue_avgpeople.data,
            queue_waitingtime = form.emigration_queue_waitingtime.data,
            sys_avgpeople = form.emigration_sys_avgpeople.data,
            sys_waitingtime = form.emigration_sys_waitingtime.data,
            waitingarea_length = form.emigration_waitingarea_length.data,
            waitingarea_breadth = form.emigration_waitingarea_breadth.data,
            avgwaitingarea_space = round(form.emigration_waitingarea_length.data*form.emigration_waitingarea_breadth.data/form.emigration_queue_avgpeople.data,1))
        
        newSecurity = Security_checkpoint(
            airport_id = form.iata_code.data,
            diag_time = form.diag_time.data,
            uti_rate = form.security_uti_rate.data,
            queue_avgpeople = form.security_queue_avgpeople.data,
            queue_waitingtime = form.security_queue_waitingtime.data,
            sys_avgpeople = form.security_sys_avgpeople.data,
            sys_waitingtime = form.security_sys_waitingtime.data,
            waitingarea_length = form.security_waitingarea_length.data,
            waitingarea_breadth = form.security_waitingarea_breadth.data,
            avgwaitingarea_space = round(form.security_waitingarea_length.data*form.security_waitingarea_breadth.data/form.security_queue_avgpeople.data,1))

        db.session.add(newCheckin)
        db.session.add(newEmigration)
        db.session.add(newSecurity)
        db.session.commit()
        return redirect(url_for('diagnostics.selection'))
    else:
        print("FAILED")
        print(form.errors)

    return render_template("diagnostics/adddiagnostics.html",
                            title = 'Add Diagnostics (Detailed)',
                            form = form)

@mod.route('/adddiagnostics_simple',methods=['POST','GET'])
@login_required
def adddiagnostics_simple():
    form = AddDiagnostics_Simple()
    if request.method == 'POST' and form.validate():

        # rho=[] # utilisation
        # Nq=[] # Number of people in the queue
        # Wq=[] # waiting time in queue
        # N=[] # Number of people in the system
        # W=[] # waiting time in system

        mms_checkin = mms(1/form.checkin_avg_interarrival.data, 1/form.checkin_avg_processing.data, 6)
        mms_emigration = mms(1/form.emigration_avg_interarrival.data, 1/form.emigration_avg_processing.data, 6)
        mms_security = mms(1/form.security_avg_interarrival.data, 1/form.security_avg_processing.data, 6)

        # print (mms_checkin)
        # print (mms_emigration)
        # print (mms_security)

        newCheckin = Check_in(
            airport_id = form.iata_code.data,
            diag_time = form.diag_time.data,
            uti_rate = mms_checkin[0],
            queue_avgpeople = mms_checkin[1],
            queue_waitingtime = mms_checkin[2],
            sys_avgpeople = mms_checkin[3],
            sys_waitingtime = mms_checkin[4],
            avgwaitingarea_space = round(form.checkin_waitingarea_length.data*form.checkin_waitingarea_breadth.data/mms_checkin[1],1),
            waitingarea_length = form.checkin_waitingarea_length.data,
            waitingarea_breadth = form.checkin_waitingarea_breadth.data,
            avg_interarrival = form.checkin_avg_interarrival.data,
            avg_processing = form.checkin_avg_processing.data)

        
        newEmigration = Emigration(
            airport_id = form.iata_code.data,
            diag_time = form.diag_time.data,
            uti_rate = mms_emigration[0],
            queue_avgpeople = mms_emigration[1],
            queue_waitingtime = mms_emigration[2],
            sys_avgpeople = mms_emigration[3],
            sys_waitingtime = mms_emigration[4],
            waitingarea_length = form.emigration_waitingarea_length.data,
            waitingarea_breadth = form.emigration_waitingarea_breadth.data,
            avgwaitingarea_space = round(form.emigration_waitingarea_length.data*form.emigration_waitingarea_breadth.data/mms_emigration[1],1),
            avg_interarrival = form.checkin_avg_interarrival.data,
            avg_processing = form.checkin_avg_processing.data)


        newSecurity = Security_checkpoint(
            airport_id = form.iata_code.data,
            diag_time = form.diag_time.data,
            uti_rate = mms_security[0],
            queue_avgpeople = mms_security[1],
            queue_waitingtime = mms_security[2],
            sys_avgpeople = mms_security[3],
            sys_waitingtime = mms_security[4],
            waitingarea_length = form.security_waitingarea_length.data,
            waitingarea_breadth = form.security_waitingarea_breadth.data,
            avgwaitingarea_space = round(form.security_waitingarea_length.data*form.security_waitingarea_breadth.data/mms_security[1],1),
            avg_interarrival = form.checkin_avg_interarrival.data,
            avg_processing = form.checkin_avg_processing.data)


        db.session.add(newCheckin)
        db.session.add(newEmigration)
        db.session.add(newSecurity)
        db.session.commit()
        return redirect(url_for('diagnostics.selection'))
    # else:
    #     print("FAILED")
    #     print(form.errors)

    return render_template("diagnostics/adddiagnostics_simple.html",
                            title = 'Add Diagnostics',
                            form = form)


@mod.route('/<airport_code>/<diag_time>/')
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
    checkin_grade_space = get_grade_space('check_in',checkin_info.avgwaitingarea_space)
    emigration_grade_space = get_grade_space('emigration',emigration_info.avgwaitingarea_space)
    security_grade_space = get_grade_space('security_checkpoint',security_info.avgwaitingarea_space)
    score = overall_grade(checkin_grade,emigration_grade,security_grade,checkin_grade_space,emigration_grade_space,security_grade_space)
    input_link = request.path + "addarea"
    checkin_link = request.path + "check_in"
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
                            checkin_grade_space = checkin_grade_space,
                            emigration_grade_space = emigration_grade_space,
                            security_grade_space = security_grade_space,
                            score = score,
                            input_link = input_link,
                            checkin_link = checkin_link)

@mod.route('/<airport_code>/<diag_time>/addarea',methods=['POST','GET'])
@login_required
def addarea(airport_code, diag_time):
    current_link = request.path
    previous_link = current_link[:-7] # Remove "/addarea"
    current_Time = datetime.datetime.strptime(diag_time, "%Y-%m-%d")
    # print (type(current_Time))
    checkin_info = Check_in.query.get((airport_code, diag_time))
    emigration_info = Emigration.query.get((airport_code, diag_time))
    security_info = Security_checkpoint.query.get((airport_code, diag_time))
    # Get IATA LoS grades of each value
    checkin_grade = get_grade('check_in',checkin_info.sys_waitingtime)
    emigration_grade = get_grade('emigration',emigration_info.sys_waitingtime)
    security_grade = get_grade('security_checkpoint',security_info.sys_waitingtime)
    checkin_grade_space = get_grade_space('check_in',checkin_info.avgwaitingarea_space)
    emigration_grade_space = get_grade_space('emigration',emigration_info.avgwaitingarea_space)
    security_grade_space = get_grade_space('security_checkpoint',security_info.avgwaitingarea_space)
    score = overall_grade(checkin_grade,emigration_grade,security_grade,checkin_grade_space,emigration_grade_space,security_grade_space)
    form = AddArea()
    if request.method == 'POST' and form.validate():
        checkin_info.waitingarea_length = form.checkin_length.data
        checkin_info.waitingarea_breadth = form.checkin_breadth.data
        checkin_info.avgwaitingarea_space = round(form.checkin_length.data*form.checkin_breadth.data/checkin_info.queue_avgpeople,1)
        emigration_info.waitingarea_length = form.emigration_length.data
        emigration_info.waitingarea_breadth = form.emigration_breadth.data
        emigration_info.avgwaitingarea_space = round(form.emigration_length.data*form.emigration_breadth.data/emigration_info.queue_avgpeople,1)
        security_info.waitingarea_length = form.security_length.data
        security_info.waitingarea_breadth = form.security_breadth.data
        security_info.avgwaitingarea_space = round(form.security_length.data*form.security_breadth.data/security_info.queue_avgpeople,1)
        db.session.commit()
        return redirect(previous_link)
    # else:
        # print("NO")
    return render_template("diagnostics/addarea.html", 
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
                            score = score,
                            form = form,
                            current_link = current_link,
                            previous_link = previous_link)

@mod.route('/<airport_code>/<diag_time>/check_in',methods=['POST','GET'])
@login_required
def check_in(airport_code, diag_time):
    current_link = request.path
    previous_link = current_link[:-7] # Remove "/addarea"
    current_Time = datetime.datetime.strptime(diag_time, "%Y-%m-%d")
    # print (type(current_Time))
    checkin_info = Check_in.query.get((airport_code, diag_time))
    emigration_info = Emigration.query.get((airport_code, diag_time))
    security_info = Security_checkpoint.query.get((airport_code, diag_time))
    # Get IATA LoS grades of each value
    checkin_grade = get_grade('check_in',checkin_info.sys_waitingtime)
    emigration_grade = get_grade('emigration',emigration_info.sys_waitingtime)
    security_grade = get_grade('security_checkpoint',security_info.sys_waitingtime)
    checkin_grade_space = get_grade_space('check_in',checkin_info.avgwaitingarea_space)
    emigration_grade_space = get_grade_space('emigration',emigration_info.avgwaitingarea_space)
    security_grade_space = get_grade_space('security_checkpoint',security_info.avgwaitingarea_space)
    score = overall_grade(checkin_grade,emigration_grade,security_grade,checkin_grade_space,emigration_grade_space,security_grade_space)
    form = AddArea()

    checkin_values = Check_in.query.get((airport_code, diag_time))
    # mms(1/checkin_values.avg_interarrival, 1/checkin_values.avg_processing, i)
    W=[]   # waiting time in system
    W_p=[] # processing time in system

    if checkin_values.avg_interarrival != 0 and checkin_values.avg_processing != 0:
        for i in range(5,11):
            # rho.append(mms(1/checkin_values.avg_interarrival, 1/checkin_values.avg_processing, i)[0])
            # Nq.append(mms(1/checkin_values.avg_interarrival, 1/checkin_values.avg_processing, i)[1])
            # Wq.append(mms(1/checkin_values.avg_interarrival, 1/checkin_values.avg_processing, i)[2])
            # N.append(mms(1/checkin_values.avg_interarrival, 1/checkin_values.avg_processing, i)[3])
            W.append(mms(1/checkin_values.avg_interarrival, 1/checkin_values.avg_processing, i)[4])

        for i in range(round(checkin_values.avg_processing)-40,round(checkin_values.avg_processing)+40,16):
            r,n1,w1,n2,w2=mms(1/checkin_values.avg_interarrival,1/(i),6)
            W_p.append(w2)

    if request.method == 'POST' and form.validate():
        checkin_info.waitingarea_length = form.checkin_length.data
        checkin_info.waitingarea_breadth = form.checkin_breadth.data
        checkin_info.avgwaitingarea_space = round(form.checkin_length.data*form.checkin_breadth.data/checkin_info.queue_avgpeople,1)
        emigration_info.waitingarea_length = form.emigration_length.data
        emigration_info.waitingarea_breadth = form.emigration_breadth.data
        emigration_info.avgwaitingarea_space = round(form.emigration_length.data*form.emigration_breadth.data/emigration_info.queue_avgpeople,1)
        security_info.waitingarea_length = form.security_length.data
        security_info.waitingarea_breadth = form.security_breadth.data
        security_info.avgwaitingarea_space = round(form.security_length.data*form.security_breadth.data/security_info.queue_avgpeople,1)
        db.session.commit()
        return redirect(previous_link)

    # print (W)
    print ("THIS IS W_P IN ACTION")
    print (W_p)
    return render_template("diagnostics/check_in.html", 
                            title = "Check-in for "+ airport_code, 
                            airport_info = Airport.query.get(airport_code),
                            diagTime = get_diagTimes(airport_code),
                            current_Time = current_Time,
                            checkin_info = checkin_info,
                            emigration_info = emigration_info,
                            security_info = security_info,
                            checkin_grade = checkin_grade,
                            emigration_grade = emigration_grade,
                            security_grade = security_grade,
                            score = score,
                            form = form,
                            current_link = current_link,
                            previous_link = previous_link,
                            W = W,
                            W_p = W_p)

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

def get_grade_space(process,area):
    space_OD_LB = Iata_los.query.get(process).space_overdesign_LB
    space_OD_UB = Iata_los.query.get(process).space_suboptimum_UB
    # print (process, area, space_OD_UB,space_OD_LB)
    if area > 0 and area < space_OD_UB: 
        result = 'Suboptimum'
    elif area > space_OD_LB:
        result = 'Over-design'
    elif area >= space_OD_UB and area <= space_OD_LB:
        result = 'Optimum'
    else:
        result = None
        # print (process,result)
    return result

def overall_grade(checkin_grade, emigration_grade, security_grade,checkin_grade_space,emigration_grade_space,security_grade_space):
    # print(checkin_grade,emigration_grade,security_grade,checkin_grade_space,emigration_grade_space,security_grade_space)
    top = process_point("check_in",checkin_grade)[0]*process_point("check_in",checkin_grade)[1] + process_point("emigration",emigration_grade)[0]*process_point("emigration",emigration_grade)[1] + process_point("security_checkpoint",security_grade)[0]*process_point("security_checkpoint",security_grade)[1] + process_point("space_check_in",checkin_grade_space)[0]*process_point("space_check_in",checkin_grade_space)[1] + process_point("space_emigration",emigration_grade_space)[0]*process_point("space_emigration",emigration_grade_space)[1] + process_point("space_security_checkpoint",security_grade_space)[0]*process_point("space_security_checkpoint",security_grade_space)[1]
    if checkin_grade_space == None and emigration_grade_space == None and security_grade_space == None:
        bottom = process_point("check_in",checkin_grade)[0] + process_point("emigration",emigration_grade)[0] + process_point("security_checkpoint",security_grade)[0]
    else:
        bottom = process_point("check_in",checkin_grade)[0] + process_point("emigration",emigration_grade)[0] + process_point("security_checkpoint",security_grade)[0] + process_point("space_check_in",checkin_grade_space)[0] + process_point("space_emigration",emigration_grade_space)[0] + process_point("space_security_checkpoint",security_grade_space)[0]
    score = top/bottom
    # print ("Score is")
    # print (score, top,bottom)
    if score >2.5:
        grade = ["A","Over-design"]
    elif score>2 and score <=2.5:
        grade = ["A","Optimum"]
    elif score<=2 and score>1:
        grade = ["B",""]
    elif score<=1:
        grade = ["C",""]
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
    else:
        points = 0
    return [weight,points]


# Average queue times

# coding: utf-8

# In[ ]:

import math


# In[ ]:

def findsig (i,s,arr,pro,rho):
    if i<0:
        raise ValueError("i cannot be negative")
    if i<=s-1:
        sig=(1/(math.factorial(i)))*((arr/pro)**i)
    elif i>=s:
        sig=((s**s)/math.factorial(s))*(rho**i)

    return sig

def mms(arr,pro,s):
    
    rho=arr/(s*pro)
    
    rho1=arr/pro
    p0inv=(s**s)/math.factorial(s)*(rho**s)/(1-rho)
    for i in range (s):
        p0inv=p0inv+(1/(math.factorial(i)))*((arr/pro)**i)
    p0=1/p0inv
    ps=p0*findsig(s,s,arr,pro,rho)
    N=arr/pro+ ps*(rho/(1-rho)**2)
    Nq=N-(arr/pro)
    Wq=Nq/arr
    W=Wq+(1/pro)

    return(round(rho,2),round(Nq,2),round(Wq,2),round(N,2),round(W,2))


# In[ ]:

rho=[] # utilisation
Nq=[]  # Number of people in the queue
Wq=[]  # waiting time in queue
N=[]   # Number of people in the system
W=[]   # waiting time in system

# for i in range(5,11):
#     rho.append(mms(1/arr_mean,1/pro_mean,i)[0])
#     Nq.append(mms(1/arr_mean,1/pro_mean,i)[1])
#     Wq.append(mms(1/arr_mean,1/pro_mean,i)[2])
#     N.append(mms(1/arr_mean,1/pro_mean,i)[3])
#     W.append(mms(1/arr_mean,1/pro_mean,i)[4])

# Average processing times

rho=[] # utilisation
Nq=[]  # Number of people in the queue
Wq=[]  # waiting time in queue
N=[]   # Number of people in the system
W=[]   # waiting time in system


# for i in range(round(pro_mean)-40,round(pro_mean)+40,16):
#     print(i)
#     r,n1,w1,n2,w2=mms(1/arr_mean,1/(i),6)
#     rho.append(r)
#     Nq.append(n1)
#     Wq.append(w1)
#     N.append(n2)
#     W.append(w2)