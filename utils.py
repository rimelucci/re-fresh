from pymongo import MongoClient
import time

import hashlib
import re

def hash(text):
        return hashlib.sha256(text).hexdigest()

def checkUsername(username):
    return not re.search('[^a-zA-Z0-9]', username) and len(username) > 0

connection = MongoClient()

db = connection['database']

"""
This method registers a customer with their email, name, and password
"""
def register_user(fullname, email, password):
    us = list(db.users.find({'email':email}))
    if us == []:
        t = {'fullname':fullname, 'email': email, 'password':password}
        db.users.insert(t)
        result = True
    else:
        result = False
    return result

"""
Prints all users
"""
def fetch_all_users():
    users = db.users.find()
    return list(users)

if __name__ == "__main__":
    db.drop_collection('users')
    print register_user('Young Kim', 'kim.thunderbird@gmail.com', 'password')
    print register_user('Derrick Lui', 'derricklui@gmail.com', 'password')
    print register_user('Young Kim', 'kim.thunderbird@gmail.com', 'password')
    print fetch_all_users()
