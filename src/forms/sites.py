from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired


class CreateSiteForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    url = StringField(validators=[DataRequired(), URL()])
    submit = SubmitField("Create")


class UpdateSiteForm(CreateSiteForm):
    submit = SubmitField("Update")
