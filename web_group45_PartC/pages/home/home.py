from flask import Blueprint, render_template, request, redirect, url_for
from db_connector import *

# routs
home = Blueprint(
    'home',
    __name__,
    static_folder='static',
    static_url_path='/home',
    template_folder='templates'
)

# routs
@home.route('/')
@home.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@home.route('/home/newsletterRegister', methods=['GET', 'POST'])
def homeRegisterFunc():
    if request.method == 'POST':
        email = request.form['email']
        insert_newsletter_email(email)
        return redirect(url_for('home.index'))