from flask import Blueprint, render_template, request, redirect, url_for
from db_connector import *

contact = Blueprint(
    'contact',
    __name__,
    static_folder='static',
    static_url_path='/contact',
    template_folder='templates'
)

@contact.route('/contact', methods=['GET','POST'])
def index():
    return render_template('contact.html')


@contact.route('/contact/form', methods=['GET','POST'])
def contactFormFunc():
    if request.method == 'POST':
        # Extract data from the form
        Flname = request.form['Flname']
        email = request.form['email']
        ILphone = request.form['ILphone']
        massage = request.form['massage']

        # Create a dictionary with message data
        message_dict = {
            'full_name': Flname,
            'email': email,
            'phone_number': ILphone,
            'message': massage
        }
        insert_message(message_dict)
        return redirect(url_for('contact.index'))


@contact.route('/contact/newsletterRegister', methods=['GET', 'POST'])
def contactRegisterFunc():
    if request.method == 'POST':
        email = request.form['email']
        insert_newsletter_email(email)
        return redirect(url_for('contact.index'))

