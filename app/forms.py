from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField()

class SearchForm(FlaskForm):
    query = StringField('Search', [DataRequired()])
    submit = SubmitField() 

class AddForm(FlaskForm):
    add_to_cart = SubmitField()