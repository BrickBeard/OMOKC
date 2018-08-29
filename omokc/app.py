import os
import sys
sys.path.insert(0, '/home/skbolay/public_html/cgi-bin/venv/lib/python3.6/site-packages')

from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message

mail = Mail()

app = Flask(__name__)
app.secret_key = 'testtest12345'

mail.init_app(app)

omEmail = 'sample_email@gmail.com'
omPhone = '(444) 123-4567'

@app.route('/')
def home():
    return render_template('index.html', omEmail=omEmail, omPhone=omPhone)

@app.route('/home')
def home1():
    return render_template('index.html', omEmail=omEmail, omPhone=omPhone)

@app.route('/info')
def info():
    return render_template('information.html', omEmail=omEmail, omPhone=omPhone)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form, omEmail=omEmail, omPhone=omPhone)
        else:
            msg = Message('Message from your OMOKC.com' + form.name.data, sender='brickbeard.io@gmail.com', recipients=['brickbeard.io@gmail.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True, omEmail=omEmail, omPhone=omPhone)
    elif request.method == 'GET':
        return render_template('contact.html', form=form, omEmail = omEmail, omPhone=omPhone)


if __name__ == '__main__':
    app.run(debug=True)
