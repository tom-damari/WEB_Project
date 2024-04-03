from flask import Blueprint, render_template, url_for, redirect
from db_connector import *

account = Blueprint(
    'account',
    __name__,
    static_folder='static',
    static_url_path='/account',
    template_folder='templates'
)

@account.route('/account')
def index():
    if session['user_email']:
        user_email = session['user_email']
        curr_customer = get_filtered_list_of_customers({'email': user_email})[0]
        order_list = get_filtered_list_of_orders({'email': user_email})
        return render_template('account.html', curr_customer=curr_customer, order_list=order_list)
    else:
        # Redirect the user to the login page or display an error message
        return redirect(url_for('login.index'))

@account.route('/logout')
def logout():
    session['logged_in'] = False
    session['user_email'] = ''
    return redirect(url_for('login.index'))