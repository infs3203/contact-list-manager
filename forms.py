from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, Length

class ContactForm(FlaskForm):
    name = StringField('Name', 
                       validators=[
                           DataRequired(message="Name is required"),
                           Regexp(r'^[A-Za-z\s]+$', message="Name should contain only letters and spaces"),
                           Length(min=2, max=50, message="Name must be between 2 and 50 characters")
                       ])
    
    phone = StringField('Phone', 
                        validators=[
                            DataRequired(message="Phone number is required"),
                            Regexp(r'^\d{10,15}$', message="Phone number must contain 10-15 digits")
                        ])
    
    email = StringField('Email', 
                        validators=[
                            DataRequired(message="Email is required"),
                            Email(message="Invalid email format")
                        ])
    
    type = SelectField('Type', 
                       choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Other', 'Other')],
                       validators=[DataRequired(message="Type is required")])
    
    submit = SubmitField('Submit')
