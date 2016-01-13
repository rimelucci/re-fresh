from pymongo import MongoClient
import hashlib
import re

connection = MongoClient()
db = connection['database']

"""
Returns hashed password

Args:
    text - string to be hashed

Returns:
    hashed string
"""
def hash(text):
    return hashlib.sha256(text).hexdigest()

"""
~~-----------------------------USERS----------------------------------------~~
"""


"""
Checks whether username is allowed

Args:
    username - string to be checked

Returns:
    True if string is allowed
    False if it is not
"""
def check_username(username):
    return not re.search('[^a-zA-Z\s]', username) and len(username) > 0


"""
Registers an user with their email, name, and password.

Args:
    fullname - string with full name
    email - user email address
    password - password for the user

Returns:
    True if user does not exist
    False if user already exists
"""
def register_user(fullname, email, password):
    check = list(db.users.find({'email':email}))
    
    if check == []:
        t = {'fullname':fullname, 'email': email, 'password':hash(password), 'inventory':[]}
        db.users.insert(t)
        print fetch_all_users()
        return True
    print fetch_all_users()
    return False

"""
Authenticates user based on email and password

Args:
    email - user email address
    password - password

Returns:
    False if user is not registered or passwords do not match
    True if password is successfully verified
"""
def authenticate_user(email, password):
    check = list(db.users.find({'email':email}))

    if check == []:                       # User does not exist
        return False
    else:                                 # Passwords do not match
        if not check[0]['password'] == hash(password):
           return False
    return True

"""
Adds an item to the user's cart
"""
def add_item(name, price):
    return

"""
Prints all users in database

Args:
    None

Returns:
    List of all users
"""
def fetch_all_users():
    users = db.users.find()
    return list(users)

"""
~~-----------------------------STORES----------------------------------------~~
"""

"""
Registers a store with name and password

Args:
    name - string with store name
    password - password for the store

Returns:
    True if store does not exist
    False if store already exists
"""
def register_store(name, email, password):
    check = list(db.stores.find({'email':email}))

    if check == []:
        t = {'name':name, 'email':email, 'password':hash(password)}
        db.stores.insert(t)
        print fetch_all_stores()
        return True
    print fetch_all_stores()
    return False

"""
Authenticates store based on name and password

Args:
    name - store name
    password - password

Returns:
    False if user is not registered or passwords do not match
    True if password is successfully verified
"""
def authenticate_store(email, password):
    check = list(db.stores.find({'email':email}))

    if check == []:
        return False
    else:
        if not check[0]['password'] == hash(password):
            return False
    return True

"""
Prints all stores in database

Args:
    None

Returns:
    List of all stores
"""
def fetch_all_stores():
    stores = db.stores.find()
    return list(stores)

"""
~~-----------------------------ITEMS----------------------------------------~~
"""

"""
Registers an item

Args:
    name - name of item
    amount - amount of item to be offered
    price - price of item
    email - email that store is registering with

Returns:
    True if store is registered
    False if store does not exist
"""
def register_item(name, amount, price, email):
    check = list(db.stores.find({'name':name, 'email':email}))

    amount = int(amount)
    
    if check == []:
        t = {'name':name, 'amount':amount, 'price':price, 'email':email}
        db.items.insert(t)
        return True
    return False

"""
Purchase an item

Args:
    name - name of item
    amount - amount if item to be bought
    price - price of item
    email - email that store used to registered with 

Returns:
    True if item exists for given amount
    False if it does not exist
"""
def purchase_item(name, amount, email):
    check = list(db.items.find({
        'name':name,
        'email':email
    }))

    price = check[0]['price']
    curr_amount = int(check[0]['amount'])
    amount = int(amount)
    difference = curr_amount-amount
    
    if amount < curr_amount:
        db.items.update(
            {
                'name':name,
                'email':email
            },
            {
                'name':name,
                'email':email,
                'price':price,
                'amount':difference
            })
        return True
    return False

"""
Prints all items in database

Args:
    None

Returns:
    List of all items
"""
def fetch_all_items():
    items = db.items.find()
    return list(items)

"""
TESTING ONLY

Resets database
"""
def reset():
    db.drop_collection('users')
    db.drop_collection('stores')
    db.drop_collection('items')
"""
------------------------TESTING-------------------
"""
if __name__ == "__main__":
    db.drop_collection('users')

    print "\n---------------TESTING REGISTER_USER-----------------\n"
    
    print register_user('Young Kim', 'kim.thunderbird@gmail.com', 'password')
    print register_user('Derrick Lui', 'derricklui@gmail.com', 'password') 
    print register_user('Young Kim', 'kim.thunderbird@gmail.com', 'password')

    print "\n---------------TESTING FETCH_ALL_USERS-----------------\n"
    
    print fetch_all_users()

    print "\n---------------TESTING AUTHENTICATE-----------------\n"
    
    print authenticate_user("kim.thunderbird@gmail.com", 'yo')
    print authenticate_user('kim.thunderbird@gmail.com', "password")

    print "\n---------------TESTING CHECK_USERNAME-----------------\n"

    print check_username("yoyo aaron")
    print check_username("@349*")

    print "\n---------------TESTING REGISTER_USER-----------------\n"

    print register_store("dan", "email", "dan")
    print register_item("apples", "2", "2.34", "email")

    print fetch_all_items()
    
    print purchase_item("apples", "1", "email")

    print fetch_all_items()
