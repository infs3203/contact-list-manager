from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError
import re
from models import Contact

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), 
        Length(min=2, message="Name must be at least 2 characters long."),
        # Custom validator to ensure name doesn't contain numbers
        Regexp(r'^[A-Za-z\s]+$', message="Name must contain only letters and spaces.")
    ])
    
    phone = StringField('Phone', validators=[
        DataRequired(), 
        Length(min=10, max=15, message="Phone number must be between 10 and 15 characters."), 
        Regexp(r'^\+?\d{10,15}$', message="Phone number must be valid.")
    ])
    
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Invalid email address.")
    ])
    
    type = SelectField('Type', choices=[
        ('Personal', 'Personal'), 
        ('Work', 'Work'), 
        ('Other', 'Other')
    ])
    
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        existing_contact = Contact.query.filter_by(phone=phone.data).first()
        if existing_contact:
            raise ValidationError('This phone number is already associated with another contact.')

    def validate_email(self, email):
        existing_contact = Contact.query.filter_by(email=email.data).first()
        if existing_contact:
            raise ValidationError('This email address is already associated with another contact.')
