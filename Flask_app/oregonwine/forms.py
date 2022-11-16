from flask_wtf import FlaskForm
from wtforms import StringField

class WineFilter(FlaskForm):
    
    category = StringField('Wine Category')



