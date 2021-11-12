#!/usr/bin/python3


from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html to continue
