from flask import Flask
import re

# ------ CREATE APPLICATION ------ #
app = Flask(__name__)
app.config.from_pyfile('settings.py')

# ------ PAGES ------ #
# about
from pages.about.about import about
app.register_blueprint(about)
# account
from pages.account.account import account
app.register_blueprint(account)
# cart
from pages.cart.cart import cart
app.register_blueprint(cart)
# catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)
# contact
from pages.contact.contact import contact
app.register_blueprint(contact)
# home
from pages.home.home import home
app.register_blueprint(home)
# log in
from pages.login.login import login
app.register_blueprint(login)
# product
from pages.product.product import product
app.register_blueprint(product)
# sign in
from pages.signin.signin import signin
app.register_blueprint(signin)

def regex_match(string, pattern):
    return re.match(pattern, string) is not None
app.jinja_env.filters['regex_match'] = regex_match

