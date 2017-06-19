import os
from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
from functools import wraps

app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.init_app(app)

from app import models
from app.views import main
from app.views import benchmarking
from app.views import diagnostics
from app.views import authentication
from app.views import metrics

app.register_blueprint(main.mod)
app.register_blueprint(benchmarking.mod)
app.register_blueprint(diagnostics.mod)
app.register_blueprint(authentication.mod)
app.register_blueprint(metrics.mod)
