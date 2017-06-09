from wtforms import Form, StringField, TextAreaField, SubmitField, validators

def CheckNameLength(form, field):
    if len(field.data) < 5:
        raise ValidationError('Message must have more than 4 characters')

class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired()])
    email = StringField("Email", [validators.DataRequired(), validators.Email('your@email.com')])
    subject = StringField("Subject")
    message = TextAreaField("Message", [validators.DataRequired(), CheckNameLength])
    submit = SubmitField("Send")
