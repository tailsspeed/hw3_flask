from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    cityname = StringField('City Name')
    submit = SubmitField('Submit')