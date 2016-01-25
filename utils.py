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
Gets the cart of a given user

Args:
  email: email of user

Return:
  cart as a list of JSON objects
"""
def get_user_cart(email):
    check = list(db.users.find({'email': email}))

    if check != []:
        cart = check[0]['inventory']
        return cart
    return []

"""
Adds an item to the user's cart

Args:
  i_name: item name
  i_email: item email (email under wich the item is registered)
  u_email: user email
  quantity: quantity of item user wishes to buy

Return:
  True if user exists
  False if user does not exist
"""
def add_cart(i_name, i_email="default", u_email, quantity):
    check = list(db.users.find({'email':u_email}))
    item = {'name': i_name, 'email': i_email, 'quantity': quantity}

    if check != []:
        original = check[0]['inventory']

        print "ORIGINAL" + str(original)
    
        original.append(item)
    
        db.users.update(
            {
                'email': u_email
            },
            {'$set':
             {
                 "inventory": original
             }
         }
        )
        return True
    return False

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

def check_store(username):
    return not re.search('[^a-zA-Z\s]', username) and len(username) > 0


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
    quantity - quantity of item to be offered
    price - price of item
    email - email that store is registering with

Returns:
    True if store is registered
    False if store does not exist
"""
def register_item(name, quantity, price, email="default"):
    check = list(db.items.find({'name':name, 'email':email}))

    quantity = int(quantity)

    if check == []:
        t = {'name':name, 'quantity':quantity, 'price':price, 'email':email}
        db.items.insert(t)
        return True
    return False

"""
Add stock to an item

Args:
    name: name of item
    quantity: quantity to add
    email: email of store

Returns:
    True if store is registered
    False if store does not exist
"""
def add_quantity(name, quantity, email="default"):
    check = list(db.items.find({
        'name':name,
        'email':email
    }))

    if not check == []:
        price = check[0]['price']
        curr_quantity = int(check[0]['quantity'])
        quantity = int(quantity)
        total = curr_quantity + quantity

        db.items.update(
            {
                'name':name,
                'email':email
            },
            {
                'name':name,
                'email':email,
                'price':price,
                'quantity':total
            })
        return True
    return False

"""
Purchase an item

Args:
    name - name of item
    quantity - quantity if item to be bought
    price - price of item
    email - email that store used to registered with 

Returns:
    True if item exists for given quantity
    False if it does not exist
"""
def purchase_item(name, quantity, email="default"):
    check = list(db.items.find({
        'name':name,
        'email':email
    }))

    if not check == []:
        price = check[0]['price']
        curr_quantity = int(check[0]['quantity'])
        quantity = int(quantity)
        difference = curr_quantity-quantity
        
        if difference == 0:
            remove_item(name,email)
        
        if quantity < curr_quantity:
            db.items.update(
                {
                    'name':name,
                    'email':email
                },
                {
                    'name':name,
                    'email':email,
                    'price':price,
                    'quantity':difference
                })
            return True
    return False

"""
Get price and quantity from name and email

Args:
    name: name of item
    email: email of store

Return:
    List of price and quantity, respectively
    False if it doesn't exist
"""

def get_item_info(name, email="default"):
    check = list(db.items.find({
        'name':name,
        'email':email
    }))

    if not check == []:
        price = check[0]['price']
        quantity = int(check[0]['quantity'])
        return [price, quantity]
    return False

"""
Removes an item from the database

Args:
    name: name of item
    email: email of store

Returns:
    None
"""
def remove_item(name, email="default"):
    db.items.remove({
        'name':name,
        'email':email
    })

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
    print "REGISTER ITEM " + str(register_item("apples", "2", "2.34", "email"))
    print register_item("chicken wings","2","3.50","email")
    print register_item("popcorn chicken","2","3.50","email")
    print register_item("roma panini","2","3.50","email")
    print register_item("bacon egg and cheese","2","3.50","email")
    print register_item("chicken quesadilla","2","3.50","email")
    print register_item("southwestern panini","2","3.50","email")
    print register_item("bacon avocado chipotle","2","3.50","email")
    print register_item("teriyaki chicken with rice","2","3.50","email")
    print register_item("chicken fajita panini","2","3.50","email")
    print register_item("bacon and cheese","2","3.50","email")
    print fetch_all_items()
    
    print purchase_item("apples", "1", "email")
    print add_quantity("apples", "1", "email")
    print get_item_info("apples", "email")

    print "\n---------------TESTING REGISTER_USER-----------------\n"

    fetch_all_users()
    add_cart('apples','email','derricklui@gmail.com',3)
    add_cart("chicken wings", "email", 'derricklui@gmail.com', 1)

    print "\n---------------TESTING REGISTER_USER-----------------\n"
    
    print get_user_cart("derricklui@gmail.com")
    print register_store("ferrys","ferrys","ferrys")
    print authenticate_store("ferrys","ferrys")
