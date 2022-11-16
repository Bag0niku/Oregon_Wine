from flask_wtf import FlaskForm
from wtforms import SelectField


class WineFilter(FlaskForm):
    
    region = SelectField('Region', choices=[])
    category = SelectField('Wine Category', choices=[])
    variety = SelectField('Variety', choices=[])
    vintage = SelectField('Vintage', choices=[])
    min_score = SelectField('Minimum Score', choices=[])
    max_score = SelectField('Maximum Score', choices=[])
    min_price = SelectField('Minimum Price', choices=[])
    max_price = SelectField('Maximum Price', choices=[])


