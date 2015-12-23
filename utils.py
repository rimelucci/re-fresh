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
Checks whether username is allowed

Args:
    username - string to be checked

Returns:
    True if string is allowed
    False if it is not
"""
def check_username(username):
    return not re.search('[^a-zA-Z0-9]', username) and len(username) > 0


"""
Registers an user with their email, name, and password.

Args:
    fullname - string with full name
    email - user email address
    password 

Returns:
    True if user does not exist
    False if user already exists
"""
def register_user(fullname, email, password):
    check = list(db.users.find({'email':email}))
    
    if check == []:
        t = {'fullname':fullname, 'email': email, 'password':hash(password)}
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
    True if password is sucessfully verified
"""
def authenticate(email, password):
    check = list(db.users.find({'email':email}))

    if check == []:                       # User does not exist
        return False
    else:                                 # Passwords do not match
        if not check[0]['password'] == hash(password):
           return False
    return True


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
    
    print authenticate("kim.thunderbird@gmail.com", 'yo')
    print authenticate('kim.thunderbird@gmail.com', "password")

    print "\n---------------TESTING CHECK_USERNAME-----------------\n"

    print check_username("yoyo123")
    print check_username("@349*")
