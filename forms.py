from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import InputRequired, DataRequired

import datetime


class OrdersForm(FlaskForm):
    name = StringField('order_id', validators=[InputRequired()])
    email = StringField('email_id', validators=[InputRequired()])
    order_date = DateField(
        "order_date", format="%Y-%m-%d",
        default=datetime.today,
        validators=[DataRequired()]
    )
    delivery_date = DateField(
        "delivery_date", format="%Y-%m-%d",
        validators=[DataRequired()]
    )
