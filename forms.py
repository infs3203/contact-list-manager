# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message="Name is required."),
        Length(min=2, max=25, message="Name must be between 2 and 25 characters."),
        Regexp(r'^[A-Za-z][A-Za-z0-9]*$', message="Name must start with a letter and can contain only letters and digits.")
    ], render_kw={"maxlength": "25"})
    phone = StringField('Phone', validators=[
        DataRequired(message="Phone number is required."),
        Regexp(r'^\+?[0-9]*$', message="Phone number must contain only digits and an optional '+' symbol.")
    ])
    email = StringField('Email', validators=[
        Email(message="Please enter a valid email address.")
    ])
    type = SelectField('Type', choices=[
        ('Personal', 'Personal'), 
        ('Work', 'Work'), 
        ('Other', 'Other')
    ])
    submit = SubmitField('Submit')