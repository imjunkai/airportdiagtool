from flask import Blueprint, render_template, redirect, flash, url_for
# from flask_login import login_required, current_user

mod = Blueprint('benchmarking', __name__, url_prefix='/benchmarking')

@mod.route('/')
# @login_required
def index():
    return render_template("benchmarking/benchmarking.html",
                            title='Benchmarking')

@mod.route('/within')
# @login_required
def bwithin():
    return render_template("benchmarking/benchmarking.html",
                            title='Benchmarking within benchmarking')