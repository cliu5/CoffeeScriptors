
import sqlite3 #imports sqlite

'''
password(username)
returns the password that matches the username if one exists
else return none
'''
def password(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    get_password = 'SELECT password FROM users WHERE users.username = (?)'
    c.execute(get_password,(username,))
    password = c.fetchone()
    return password

'''
username(username)
returns an empty list if username doesn't exist in the database
returns [username] if username exists
'''
def username(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    user_exists = 'SELECT username FROM users WHERE users.username = (?);'
    c.execute(user_exists,(username,))
    userList = c.fetchall()
    return userList

    
    
    
        
        
