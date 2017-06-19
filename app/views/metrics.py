from flask import Blueprint, render_template, redirect, flash, url_for
# from flask_login import login_required, current_user

mod = Blueprint('metrics', __name__, url_prefix='/metrics')

@mod.route('/')
# @login_required
def index():
    return render_template("metrics/metrics.html",
                            title='Metrics')

# @mod.route('/within')
# # @login_required
# def bwithin():
#     return render_template("benchmarking/benchmarking.html",
#                             title='Benchmarking within benchmarking')