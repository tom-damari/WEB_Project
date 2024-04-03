from flask import Blueprint, render_template, request, redirect, url_for, session
from db_connector import *

login = Blueprint(
    'login',
    __name__,
    static_folder='static',
    static_url_path='/login',
    template_folder='templates'
)

@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password']

        customers = get_filtered_list_of_customers({'email': email})
        if customers:
            customer = customers[0]
            if customer['password'] == password:
                session['user_email'] = email
                session['logged_in'] = True
                session['user_cart_items'] = get_user_cart(email)['items']
                return redirect(url_for('home.index', user_email=email))
            else:
                message = 'סיסמה שגויה, אנא נסה שנית'
                return render_template('login.html', message=message)
        else:
            message = 'אין משתמש רשום עם כתובת מייל זו במערכת'
            return render_template('login.html', message=message)
    else:
        return render_template('login.html')

@login.route('/forgotPassword')
def forgotPassword():
    message = 'איפוס סיסמה לא ימומש בחלק זה'
    return render_template('login.html', message=message)
