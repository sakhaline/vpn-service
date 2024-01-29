from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginUserForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField("Log in")


class RegisterUserForm(LoginUserForm):
    email = EmailField(validators=[DataRequired()])
    submit = SubmitField("Sign up")


class UpdateUserForm(LoginUserForm):
    submit = SubmitField("Submit")
