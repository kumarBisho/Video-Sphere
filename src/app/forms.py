from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class VideoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = StringField('Description', validators=[Length(max=2000)])
    url = StringField('Video URL', validators=[DataRequired(), URL()])
    duration = StringField('Duration', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Save')

