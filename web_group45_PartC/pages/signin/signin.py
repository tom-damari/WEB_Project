from flask import Blueprint, url_for
from flask import render_template, request, redirect
from db_connector import *

signin = Blueprint(
    'signin',
    __name__,
    static_folder='static',
    static_url_path='/signin',
    template_folder='templates'
)

@signin.route('/signin', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        Fname = request.form['Fname']
        Lname = request.form['Lname']
        email = request.form['email']
        ILphone = request.form['ILphone']
        password = request.form['password']
        bday = request.form['bday']

        # check that email is unique
        if len(get_filtered_list_of_customers({'email': email})) > 0:
            message = 'ההרשמה נכשלה כי כתובת מייל זו כבר רשומה במערכת למשתמש אחר'
            # flash('This email address is already registered. Please try another or reset password.', 'error')
            return render_template('signin.html', message=message) # now login to your new account
        else:
            signin_dict = {
                'firstName': Fname,
                'lastName': Lname,
                'email': email,
                'phoneNumber': ILphone,
                'password': password,
                'birthdate': bday
            }
            insert_customer(signin_dict)

            return redirect(url_for("login.index")) # now login to your new account
    else:
        return render_template('signin.html')