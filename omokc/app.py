from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message

mail = Mail()

app = Flask(__name__)
app.secret_key = 'K&Dj83*@k)jh!lJ;l_x'

mail.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home1():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('information.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message('Message from your OMOKC.com' + form.name.data, sender='brickbeard.io@gmail.com', recipients=['brickbeard.io@gmail.com', 'brandonsmith.brick@gmail.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
