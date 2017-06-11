from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(FlaskForm):
    name = TextField("Name", [validators.DataRequired('Please enter your name.')])
    email = TextField("Email", [validators.DataRequired('Please enter your email.'), validators.Email('Please enter your email.')])
    # subject = StringField("Subject")
    message = TextAreaField("Message", [validators.DataRequired('Please enter a message.')])
    submit = SubmitField("Send")
