from flask import Blueprint, render_template, redirect, url_for, request
from db_connector import *

catalog = Blueprint(
    'catalog',
    __name__,
    static_folder='static',
    static_url_path='/catalog',
    template_folder='templates'
)

from flask import Blueprint, render_template, redirect, url_for
from db_connector import *

catalog = Blueprint(
    'catalog',
    __name__,
    static_folder='static',
    static_url_path='/catalog',
    template_folder='templates'
)

@catalog.route('/catalog/<category>/<sort>')
@catalog.route('/catalog/<category>')
def index(category, sort=None):
    if category not in ['ceramics', 'jewellery']:
        return redirect(url_for('home.index'))  # Redirect to home if category is invalid
    else:
        sortQuery = {'category': category}
        if sort == 'asc':
            items = list(products_col.find(sortQuery).sort('price'))
        elif sort == 'desc':
            items = list(products_col.find(sortQuery).sort('price', -1))
        else:
            items = get_filtered_list_of_products(sortQuery)
    return render_template('catalog.html', category=category, items=items)

@catalog.route('/catalog/<category>/addItemToCart/<productName>')
def addItemToCart(category, productName):
    user_email = session.get('user_email')
    guest_id = session.get('guest_id')
    if user_email:
        add_item_to_user_cart(user_email, productName)
    elif guest_id:
        add_item_to_guest_cart(guest_id, productName)
    return redirect(url_for('.index', category=category))



# @catalog.route('/catalog/<category>')
# def index(category):
#     if category not in ['ceramics', 'jewellery']:
#         return redirect(url_for('home.index'))  # Redirect to home if category is invalid
#     items = get_filtered_list_of_products({'category': category})
#     return render_template('catalog.html', category=category, items=items)
#

# @catalog.route('/catalog/<category>/<sort>')
# def sorted_index(category, sort):
#     if category not in ['ceramics', 'jewellery']:
#         return redirect(url_for('home.index'))  # Redirect to home if category is invalid
#     sort_query = {'category': category}
#     if sort == 'ascending':
#         items = list(products_col.find(sort_query).sort('price'))
#     elif sort == 'descending':
#         items = list(products_col.find(sort_query).sort('price', -1))
#     else:
#         items = list(products_col.find(sort_query))
#     return render_template('catalog.html', category=category, items=items)

# @catalog.route('/catalog/<category>')
# def index(category, items=None):
#     if category not in ['ceramics', 'jewellery']:
#         return redirect(url_for('home.index'))  # Redirect to home if category is invalid
#     if items is None:
#         items = get_filtered_list_of_products({'category': category})
#     return render_template('catalog.html', category=category, items=items)
#
# @catalog.route('/catalog/<category>/ascending')
# def asc(category):
#     if category not in ['ceramics', 'jewellery']:
#         return redirect(url_for('home.index'))  # Redirect to home if category is invalid
#     items = list(products_col.find({'category': category}).sort('price'))
#     return redirect(url_for('.index', category=category, items=items))
#
# @catalog.route('/catalog/<category>/descending')
# def desc(category):
#     if category not in ['ceramics', 'jewellery']:
#         return redirect(url_for('home.index'))  # Redirect to home if category is invalid
#     items = list(products_col.find({'category': category}).sort('price', -1))
#     return redirect(url_for('.index', category=category, items=items))

