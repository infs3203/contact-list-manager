# from flask_wtf import FlaskForm
# from wtforms import StringField, SelectField, SubmitField

# class ContactForm(FlaskForm):
#     name = StringField('Name')
#     phone = StringField('Phone')
#     email = StringField('Email')
#     type = SelectField('Type', 
#                       choices=[('Personal', 'Personal'), 
#                               ('Work', 'Work'), 
#                               ('Other', 'Other')])
#     submit = SubmitField('Submit') 

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp(r'^\d+$', message="Phone number must contain only digits.")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email format.")])
    type = SelectField('Type', choices=[('personal', 'Personal'), ('work', 'Work'), ('other', 'Other')], validators=[DataRequired()])
    submit = SubmitField('Submit')
