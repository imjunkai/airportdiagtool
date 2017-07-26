from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_required
from app.models import Metric
from app.forms import EditWeights
from app import db

mod = Blueprint('metrics', __name__, url_prefix='/metrics')

@mod.route('/')
@login_required
def index():
    checkin_info = Metric.query.get("check_in")
    emigration_info = Metric.query.get("emigration")
    security_info = Metric.query.get("security_checkpoint")
    return render_template("metrics/metrics.html",
                            title='Metrics',
                            checkin_info = checkin_info,
                            emigration_info = emigration_info,
                            security_info = security_info)

@mod.route('/editweights', methods=['GET', 'POST'])
@login_required
def editweights():
    checkin_info = Metric.query.get("check_in")
    emigration_info = Metric.query.get("emigration")
    security_info = Metric.query.get("security_checkpoint")
    form = EditWeights()

    if request.method == 'POST' and form.validate():
        db_checkin = Metric.query.filter(Metric.process == "check_in").one()
        db_checkin.weight = form.checkin_weight.data
        db_checkin.p_overdesign = form.checkin_p_overdesign.data
        db_checkin.p_optimum = form.checkin_p_optimum.data
        db_checkin.p_suboptimum = form.checkin_p_suboptimum.data
        db_emigration = Metric.query.filter(Metric.process == "emigration").one()
        db_emigration.weight = form.emigration_weight.data
        db_emigration.p_overdesign = form.emigration_p_overdesign.data
        db_emigration.p_optimum = form.emigration_p_optimum.data
        db_emigration.p_suboptimum = form.emigration_p_suboptimum.data
        db_security = Metric.query.filter(Metric.process == "security_checkpoint").one()
        db_security.weight = form.security_weight.data
        db_security.p_overdesign = form.security_p_overdesign.data
        db_security.p_optimum = form.security_p_optimum.data
        db_security.p_suboptimum = form.security_p_suboptimum.data
        db.session.commit()
        return redirect(url_for('metrics.index'))
    else:
        print("NOPE")
    return render_template("metrics/editweights.html",
                            title='Metrics',
                            checkin_info = checkin_info,
                            emigration_info = emigration_info,
                            security_info = security_info,
                            form = form)