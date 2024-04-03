from flask import Blueprint, render_template, redirect, url_for
from db_connector import *

product = Blueprint(
    'product',
    __name__,
    static_folder='static',
    static_url_path='/product',
    template_folder='templates'
)

@product.route('/product/<category>/<product_name>')
def index(category, product_name):
    if category not in ('ceramics', 'jewellery'):
        return redirect(url_for('home.index'))
    else:
        product = products_col.find_one({'category': category, 'productName': product_name})
        if product is None:
            return redirect(url_for('catalog.index', category=category))
        else:
            return render_template('product.html', category=category, product=product)

@product.route('/product/<category>/<product_name>/addToCart')
def addProductToCart(category, product_name):
    user_email = session.get('user_email')
    guest_id = session.get('guest_id')
    pro = get_filtered_list_of_products({'productName': product_name})[0]
    if pro['status'] == 'זמין':
        if user_email:
            add_item_to_user_cart(user_email, product_name)
            user_cart = get_user_cart(user_email)
            update_total_amount(user_cart['_id'])
        elif guest_id:
            add_item_to_guest_cart(guest_id, product_name)
            update_total_amount(guest_id)
    return redirect(url_for('.index', category=category, product_name=product_name))


