from flask import Blueprint, render_template, redirect, url_for

from db_connector import *

cart = Blueprint(
    'cart',
    __name__,
    static_folder='static',
    static_url_path='/cart',
    template_folder='templates'
)

@cart.route('/cart')
def index():
    email = session.get('user_email')
    is_logged_in = session.get('logged_in', False)
    if is_logged_in:
        cart = get_user_cart(email)
        update_total_amount(cart["_id"])
        cart_data = get_user_cart(email)
    else:
        guest_cart_id, guest_cart_items = get_or_create_guest_cart()
        update_total_amount(guest_cart_id)
        cart_data = guest_carts_col.find_one({'_id': guest_cart_id})
    return render_template('cart.html', cart_data=cart_data, is_logged_in=is_logged_in)

@cart.route('/cart/removeProduct/<cart_id>/<product_name>')
def removeProduct(cart_id, product_name):
    product = get_filtered_list_of_products({'productName': product_name})[0]
    if cart_id and product:
        if session.get('guest_cart_id') and cart_id == session['guest_cart_id']:
            remove_product_from_guest_cart(cart_id, product_name)
        elif session.get('logged_in'):
            user_email = session.get('user_email')
            remove_product_from_user_cart(user_email, product_name)
    return redirect(url_for('cart.index'))

@cart.route('/cart/removeItem/<cart_id>/<product_name>')
def removeItem(cart_id, product_name):
    product = get_filtered_list_of_products({'productName': product_name})[0]
    if cart_id and product:
        if session.get('guest_cart_id') and cart_id == session['guest_cart_id']:
            remove_item_from_guest_cart(cart_id, product_name)
        elif session.get('logged_in'):
            user_email = session.get('user_email')
            remove_item_from_user_cart(user_email, product_name)
    return redirect(url_for('cart.index'))

@cart.route('/cart/addItem/<cart_id>/<product_name>')
def addItem(cart_id, product_name):
    product = get_filtered_list_of_products({'productName': product_name})[0]
    if cart_id and product:
        if session.get('guest_cart_id') and cart_id == session['guest_cart_id']:
            add_item_to_guest_cart(cart_id, product_name)
        elif session.get('logged_in'):
            user_email = session.get('user_email')
            add_item_to_user_cart(user_email, product_name)
    return redirect(url_for('cart.index'))

@cart.route('/cart/checkout/<cart_id>')
def checkout(cart_id):
    if cart_id:
        if session.get('guest_cart_id') and cart_id == session['guest_cart_id']:
            return redirect(url_for('login.index')) # Redirect to login if it's a guest cart
        elif session.get('logged_in'):
            user_email = session.get('user_email')
            checkout_user_cart(user_email) # Perform checkout for user cart
            return redirect(url_for('home.index'))

