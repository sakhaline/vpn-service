from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateSiteForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    original_url = StringField(validators=[DataRequired()])
    submit = SubmitField("Create")


class UpdateSiteForm(CreateSiteForm):
    submit = SubmitField("Update")
