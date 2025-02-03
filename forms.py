from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Name is required"), Length(min=1, max=100)])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit')

