from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    itemToFind = StringField('search', validators=[DataRequired()])
    priceFrom = FloatField('price_from')
    priceTo = FloatField('price_to')
    submit = SubmitField('submit')