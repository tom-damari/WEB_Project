import os
from datetime import datetime
from flask import session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from uuid import uuid4

##### MongoDB #####
uri = os.environ.get('DB_URI')
# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))
# create db and collections
my_database = cluster['my_database']
customers_col = my_database['customers']
products_col = my_database['products']
messages_col = my_database['messages']
orders_col = my_database['orders']
guest_carts_col = my_database['guest_carts']
user_carts_col = my_database['user_carts']
newsletter_emails_col = my_database['newsletter_emails']


# NEWSLETTER
def insert_newsletter_email(email):
    is_registered = list(newsletter_emails_col.find({'email': email}))
    if is_registered is None or len(is_registered) == 0:
        newsletter_emails_col.insert_one({'email': email, 'joinDate:': datetime.now()})


# CUSTOMERS
def get_list_of_customers():
    return list(customers_col.find())
def get_filtered_list_of_customers(query):
    return list(customers_col.find(query))
def insert_customer(customer_dict):
    customers_col.insert_one(customer_dict)
    user_carts_col.insert_one({
        'user_email': customer_dict['email'],
        'items': [],
        'totalAmount': 0
    })
def get_list_of_users():
    users_list = []
    customers = get_list_of_customers()
    for customer in customers:
        users_list.append({'email': customer['email'], 'password': customer['password']})
    return users_list


# PRODUCTS
def get_list_of_products():
    return list(products_col.find())
def get_filtered_list_of_products(query):
    return list(products_col.find(query))


# MASSAGES
def insert_message(message_dict):
    messages_col.insert_one(message_dict)


# USER CART

def get_user_cart(email):
    user_cart = user_carts_col.find_one({'email': email})
    user_cart_id = user_cart.get('_id')
    if user_cart:
        update_total_amount(user_cart_id)
    return user_cart
def add_item_to_user_cart(email, productName):
    product = products_col.find_one({"productName": productName})
    cart = get_user_cart(email)
    # get item's quantity
    quantity = 0
    for item in cart['items']:
        if item['productName'] == productName:
            quantity = item['quantity']
    if product:
        price = product.get('price', 0)
        if quantity == 0:
            # If the item is not already in the cart, add it
            item = {"productName": productName, "quantity": 1, "price": price, "sumPrice": price, "maxAmount": product['maxAmount'],
                    "photoPath": product['photoPath'][0],
                    "status": product['status']}
            user_carts_col.update_one(
                {"email": email},
                {"$push": {"items": item}},
                upsert=True
            )
        else:
            if product['category'] == 'jewellery':
                # If the item is already in the cart, update its quantity and sumPrice
                user_carts_col.update_one(
                    {"email": email, "items.productName": productName},
                    {"$set": {"items.$.quantity": quantity + 1,
                              "items.$.sumPrice": (quantity + 1) * product['price']}}
                )
        # Retrieve the updated user cart
        user_cart = get_user_cart(email)
        # Convert ObjectId to string for JSON serialization
        user_cart['_id'] = str(user_cart['_id'])
        # Store the modified user cart in the session
        session['user_cart_items'] = user_cart['items']
        # Update the total amount
        update_total_amount(user_cart.get('_id'))
def remove_item_from_user_cart(email, productName):
    product = products_col.find_one({"productName": productName})
    user_cart = get_user_cart(email)

    if user_cart and product:
        item_to_remove = None
        for item in user_cart['items']:
            if item['productName'] == productName:
                item_to_remove = item
                break
        if item_to_remove:
            # Decrease quantity and update sumPrice
            user_carts_col.update_one(
                {"email": email, "items.productName": productName},
                {"$inc": {"items.$.quantity": -1, "items.$.sumPrice": -product.get('price', 0)}},
            )
            # Remove item if quantity becomes zero
            if item_to_remove['quantity'] <= 1:
                user_carts_col.update_one(
                    {"email": email},
                    {"$pull": {"items": {'productName': productName}}},
                )
            # Retrieve the updated user cart
            user_cart = get_user_cart(email)
            # Convert ObjectId to string for JSON serialization
            user_cart['_id'] = str(user_cart['_id'])
            # Update session with the modified user cart
            session['user_cart_items'] = user_cart['items']
            # Update the total amount
            update_total_amount(user_cart.get('_id'))
def remove_product_from_user_cart(email, productName):
    user_cart = get_user_cart(email)
    product = products_col.find_one({"productName": productName})

    if user_cart and product:
        item_to_remove = None
        for item in user_cart['items']:
            if item['productName'] == productName:
                item_to_remove = item
                break
        if item_to_remove:
            user_carts_col.update_one(
                {"email": email},
                {"$pull": {"items": {'productName': productName}}},
            )
            # Retrieve the updated user cart
            user_cart = get_user_cart(email)
            # Convert ObjectId to string for JSON serialization
            user_cart['_id'] = str(user_cart['_id'])
            # Update session with the modified user cart
            session['user_cart_items'] = user_cart['items']
            # Update the total amount
            update_total_amount(user_cart.get('_id'))


# CART
def get_product_quantity_in_cart(cart_id, product_name):
    user_cart = guest_carts_col.find_one({"_id": cart_id})
    if user_cart:
        for item in user_cart['items']:
            if item['productName'] == product_name:
                return item['quantity']
    return 0

def update_product_quantity_in_cart(cart_id, productName, quantity):
    user_cart = user_carts_col.find_one({"_id": cart_id})
    guest_cart = guest_carts_col.find_one({"_id": cart_id})

    if guest_cart:
        if quantity > 0:
            guest_carts_col.update_one(
                {"_id": cart_id, "items": {'productName': productName}},
                {"$set": {"items.$.quantity": quantity}}
            )
        else:
            remove_product_from_guest_cart(cart_id, productName)
    elif user_cart:
        if quantity > 0:
            user_carts_col.update_one(
                {"_id": cart_id, "items": {'productName': productName}},
                {"$set": {"items.$.quantity": quantity}}
            )
        else:
            remove_product_from_user_cart(user_cart['email'], productName)
        update_total_amount(cart_id)

def update_total_amount(cart_id):
    user_cart = user_carts_col.find_one({"_id": cart_id})
    guest_cart = guest_carts_col.find_one({"_id": cart_id})
    total_amount = 0

    if guest_cart:
        total_amount = sum(item.get('sumPrice', 0) for item in guest_cart.get('items', []) if
                           isinstance(item.get('sumPrice'), (int, float)))
        if 'totalAmount' not in guest_cart:
            guest_cart['totalAmount'] = total_amount

        guest_carts_col.update_one(
            {"_id": cart_id},
            {"$set": {"totalAmount": total_amount}}
        )
    elif user_cart:
        total_amount = sum(item.get('sumPrice', 0) for item in user_cart.get('items', []) if
                           isinstance(item.get('sumPrice'), (int, float)))
        if 'totalAmount' not in user_cart:
            user_cart['totalAmount'] = total_amount

        user_carts_col.update_one(
            {"_id": cart_id},
            {"$set": {"totalAmount": total_amount}}
        )


# ORDERS
def get_filtered_list_of_orders(query):
    return list(orders_col.find(query))
def checkout_user_cart (email):
    cart = user_carts_col.find_one({"email": email})
    items = cart['items']
    if (items): # there are items in the cart
        newOrder = {
        "email": email,
        "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "status": "נשלח",
        "totalAmount": cart['totalAmount'],
        "items": cart['items']
        }
        orders_col.insert_one(newOrder)

        # Update maxAmount and status of products
        for item in items:
            productName = item['productName']
            quantity = item['quantity']
            product = products_col.find_one({"productName": productName})
            max_amount = product['maxAmount']
            new_max_amount = max_amount - quantity
            new_status = "נמכר" if new_max_amount == 0 else "זמין"
            products_col.update_one({"productName": productName}, {"$set": {"maxAmount": new_max_amount, "status": new_status}})

            # Update user's cart
            user_carts_col.update_many({"items.productName": productName},
                                       {"$set": {"items.$.quantity": 0, "items.$.status": 'נמכר'}})

            # Update guest carts
            guest_carts_col.update_many({"items.productName": productName},
                                        {"$set": {"items.$.quantity": 0, "items.$.status": 'נמכר'}})

            # update the cart session of user
            user_carts_col.update_one({"email": email}, {"$set": {"items": [], "totalAmount": 0}})
            # Get the updated cart document
            updated_cart = user_carts_col.find_one({"email": email})
            updated_cart_items = updated_cart['items']
            # Update session with the modified user cart items
            session['user_cart_items'] = updated_cart_items

# GUESTS
def get_or_create_guest_cart():
    if 'guest_cart_id' not in session:
        # Generate a unique identifier for the guest cart
        session['guest_cart_id'] = str(uuid4())
        session['guest_cart_items'] = []  # Initialize an empty cart
    return session['guest_cart_id'], session['guest_cart_items']

def add_item_to_guest_cart(guest_id, productName):
    product = products_col.find_one({"productName": productName})
    session['guest_cart_id'], session['guest_cart_items'] = get_or_create_guest_cart()
    quantity = get_product_quantity_in_cart(guest_id, productName)
    if product:
        if quantity == 0:
            price = product['price']
            item = {"productName": productName, "quantity": 1, "price": price, "sumPrice": price, "maxAmount": product['maxAmount'],
                    "photoPath": product['photoPath'][0],
                    "status": product['status']}
            guest_carts_col.update_one(
                {"_id": guest_id},
                {"$push": {"items": item}},
                upsert=True
            )
        else:
            if product['category'] == 'jewellery':
                # Increase quantity and update sumPrice
                guest_carts_col.update_one(
                    {"_id": guest_id, "items.productName": productName},
                    {"$inc": {"items.$.quantity": 1, "items.$.sumPrice": product['price']}},
                )
        update_total_amount(guest_id)
        # Update session with the modified guest cart
        guest_cart = guest_carts_col.find_one({"_id": guest_id})
        session['guest_cart_items'] = guest_cart['items']
def remove_item_from_guest_cart(guest_id, productName):
    guest_cart = guest_carts_col.find_one({"_id": guest_id})
    if guest_cart:
        item_to_remove = None
        for item in guest_cart['items']:
            if item['productName'] == productName:
                item_to_remove = item
                break

        if item_to_remove:
            # Decrease quantity and update sumPrice
            guest_carts_col.update_one(
                {"_id": guest_id, "items.productName": productName},
                {"$inc": {"items.$.quantity": -1, "items.$.sumPrice": -item_to_remove['price']}},
            )
            # Remove item if quantity becomes zero
            if item_to_remove['quantity'] <= 1:
                guest_carts_col.update_one(
                    {"_id": guest_id},
                    {"$pull": {"items": {'productName': productName}}},
                )
            update_total_amount(guest_id)
            # Update session with the modified guest cart
            guest_cart = guest_carts_col.find_one({"_id": guest_id})
            session['guest_cart_items'] = guest_cart['items']
def remove_product_from_guest_cart(guest_id, productName):
    guest_cart = guest_carts_col.find_one({"_id": guest_id})
    if guest_cart:
        item_to_remove = None
        for item in guest_cart['items']:
            if item['productName'] == productName:
                item_to_remove = item
                break

        if item_to_remove:
            guest_carts_col.update_one(
                {"_id": guest_id},
                {"$pull": {"items": {'productName': productName}}},
            )
            update_total_amount(guest_id)
            # Update session with the modified guest cart
            guest_cart = guest_carts_col.find_one({"_id": guest_id})
            session['guest_cart_items'] = guest_cart['items']

# GUEST CART
def generate_guest_id():
    return str(uuid4())

def create_guest_cart():
    guest_id = generate_guest_id()
    cart = {
        '_id': guest_id,
        'items': [],
        'totalAmount': 0
    }
    guest_carts_col.insert_one(cart)
    return guest_id

def associate_guest_cart_with_customer(guest_id, email):
    guest_carts_col.update_one({'_id': guest_id}, {'$set': {'email': email}})

def merge_guest_cart_with_user_cart(guest_id, user_email):
    guest_cart = guest_carts_col.find_one_and_delete({'_id': guest_id})
    if guest_cart:
        user_cart = user_carts_col.find_one({'email': user_email})
        if user_cart:
            # Merge guest cart items with user cart items
            user_carts_col.update_one({'email': user_email}, {'$push': {'items': {'$each': guest_cart['items']}}})
        else:
            # If user doesn't have a cart, create one and transfer guest cart items
            user_carts_col.insert_one({'email': user_email, 'items': guest_cart['items'], 'totalAmount': guest_cart['totalAmount']})
