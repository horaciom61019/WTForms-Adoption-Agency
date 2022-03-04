from email import message
from random import choice, choices
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter Pet's name")])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Please enter a valid URL.")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    " Form for editing an existing pet "

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")
