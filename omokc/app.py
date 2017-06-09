from flask import Flask, render_template, request
from flask_mail import Mail, Message as MailMessage
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'K&Dj83*@k)jh!lJ;l_x'

# Mail Configuration
app.config['Mail_Server'] = 'smtp.gmail.com'
app.config['Mail_PORT'] = 465
app.config['Mail_USE_SSL'] = True
app.config['Mail_USERNAME'] = 'brickbeard.io@gmail.com'
app.config['MAIL_PASSWORD'] = 'C0d1ty08'
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home1():
    return render_template('index.html')

# @app.route('/<string:page_name>/')
# def static_page(page_name):
#     return render_template('%s.html' % page_name)

@app.route('/info')
def info():
    return render_template('information.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    args = {'form': form}
    if request.method == "POST":
        if form.validate() == False:
            return "Please fill in all fields <p><a href='/contact' class='btn btn-default'>Try Again!</a></p>"
        else:
            msg = Message('Message from your OMOKC.com' + form.name.data, sender='brickbeard.io@gmail.com', recipients=['brickbeard.io@gmail.com', 'brandonsmith.brick@gmail.com'])
            msg.body = "From: %s <%s>, %s" % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return "Message Sent!"
    else:
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
