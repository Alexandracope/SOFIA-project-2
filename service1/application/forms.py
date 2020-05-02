from flask_wtf import FlaskForm
from application import db
from wtforms import submitField 
from application.models import result 

class generateForm(FlaskForm):
    submit = submitFeild('Generate')