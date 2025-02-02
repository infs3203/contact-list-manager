from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class ContactForm(FlaskForm):
    first = StringField('First Name')
    last = StringField('Last Name')
    phone = StringField('Phone')
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 