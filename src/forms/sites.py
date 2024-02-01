from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class CreateSiteForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    url = StringField(validators=[DataRequired(), URL()])
    submit = SubmitField("Create")


class UpdateSiteForm(CreateSiteForm):
    submit = SubmitField("Update")
