from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField, SubmitField


class WineFilter(FlaskForm):
    
##  The wine filter parameters
    winery_select = SelectField('Winery', choices=[])
    winery_bool = BooleanField()
    region_select = SelectField('Region', choices=[])
    region_bool = BooleanField()
    category_select = SelectField('Wine Category', choices=[])
    category_bool = BooleanField()
    variety_select = SelectField('Variety', choices=[])
    variety_bool = BooleanField()
    vintage_select = SelectField('Vintage', choices=[])
    vintage_bool = BooleanField()
    min_score_select = SelectField('Minimum Score', choices=[])
    min_score_bool = BooleanField()
    max_score_select = SelectField('Maximum Score', choices=[])
    max_score_bool = BooleanField()
    min_price_select = SelectField('Minimum Price', choices=[])
    min_price_bool = BooleanField()
    max_price_select = SelectField('Maximum Price', choices=[])
    max_price_bool = BooleanField()

## The sort results parameters
    sort_by = SelectField("How would you like the results sorted?", choices=["release_price", "score", "region", "vintage", "variety", "winery", "category"])
    sort_by_bool = BooleanField("Ascending")
    sort_desc_bool = BooleanField("Descending")

    filter_submit = SubmitField("Apply Search Parameters")


