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
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                               ('Work', 'Work'), 
                               ('Other', 'Other')],
                      validators=[DataRequired()])
    submit = SubmitField('Submit')
