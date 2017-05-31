from flask import Blueprint, render_template
from flask_login import login_required, current_user

mod = Blueprint('main',__name__)

@mod.route('/')
@login_required
def index():
	return render_template('main/index.html')
