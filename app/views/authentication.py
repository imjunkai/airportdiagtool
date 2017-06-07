from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from app import login_manager
from flask_login import login_required, current_user, login_user, logout_user
from app.models import User
from app.forms import LoginForm

mod = Blueprint('authentication',__name__, url_prefix="/authentication")

login_manager.login_view = 'authentication.login'

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
    
@mod.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.get(form.username.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            # flash('Logged In Successfully')
            return redirect(url_for('main.index'))
            # return render_template('main/dashboard.html')
        else:
            flash('Invalid Username or Password')
    return render_template('authentication/login.html', form=form)

@mod.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were just logged out!')
    return redirect(url_for('authentication.login'))


# # login required decorator
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('login'))
#     return wrap