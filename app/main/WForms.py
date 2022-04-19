from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

# Name Form using FlasForm as parent class
class nameForm(FlaskForm):
    name = StringField('What is your Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')