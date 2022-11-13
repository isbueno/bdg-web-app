from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class DnaForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    sequencia = StringField("SEQUÊNCIA", validators=[DataRequired()])
