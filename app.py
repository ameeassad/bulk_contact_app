from flask import Flask, request, render_template
from scraper_contact import add_contacts, send_inmails

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inmail')
def inmail():
    return render_template('inmail.html')

@app.route('/inmail', methods=['POST'])
def inmail_post():
    subject = request.form['subject']
    text = request.form['text']
    print(subject, text)
    send_inmails(subject,text)

    return render_template('success.html')

@app.route('/contact-req')
def contact_req():
    return render_template('contact-request.html')

@app.route('/contact-req', methods=['POST'])
def contact__req_post():
    text = request.form['text']
    add_contacts(text)

    return render_template('success.html')

@app.route('/success')
def success():
    return render_template('success.html')