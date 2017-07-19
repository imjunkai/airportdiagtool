from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required
from app.models import Metric

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

# @mod.route('/within')
# # @login_required
# def bwithin():
#     return render_template("benchmarking/benchmarking.html",
#                             title='Benchmarking within benchmarking')