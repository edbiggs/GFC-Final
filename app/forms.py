from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, Length, Regexp

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [
        DataRequired(),
        Length(min=3, max=20, message="Username must be between 3 and 20 characters"),
        Regexp('^[A-Za-z0-9_]+$', message="Username can only contain letters, numbers, and underscores")
    ])
    email = StringField('Email', validators = [
        DataRequired(),
        Email(message="Please enter a valid email address")
    ])
    password = PasswordField('Password', validators = [
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long"),
        Regexp('(?=.*\d)(?=.*[a-z])(?=.*[A-Z])', message="Password must include at least one uppercase letter, one lowercase letter, and one number")
    ])
    confirm_password = PasswordField('Confirm Password', validators = [
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [
        DataRequired(),
        Length(min=3, max=20, message="Username must be between 3 and 20 characters")
    ])
    password = PasswordField('Password', validators = [
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long")
    ])
    submit = SubmitField()

class SearchForm(FlaskForm):
    query = StringField('Search', validators = [
        DataRequired(),
        Length(min=1, max=100, message="Search query must be between 1 and 100 characters")
    ])
    submit = SubmitField()

class AddForm(FlaskForm):
    add_to_cart = SubmitField()