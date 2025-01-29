from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FileField, DateField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    profile_picture = FileField('Profile Picture')  # To upload an image
    address = StringField('Address')
    birthday = DateField('Birthday', format='%Y-%m-%d')
    
    submit = SubmitField('Submit')
