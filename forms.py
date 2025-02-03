from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message="Name is required."),
        Length(min=2, max=100, message="Name must be between 2 and 100 characters."),
        Regexp(r'^[A-Za-z][A-Za-z0-9]*$', message="Name must start with a letter and can contain only letters and digits.")
    ])
    phone = StringField('Phone')
    email = StringField('Email')
    type = SelectField('Type', choices=[
        ('Personal', 'Personal'), 
        ('Work', 'Work'), 
        ('Other', 'Other')
    ])
    submit = SubmitField('Submit')
