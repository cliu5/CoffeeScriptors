
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

'''
getAvatar(username)
returns an empty list if username doesn't exist in the database
returns [avatar] if username exists
'''
def getAvatar(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    getAva = 'SELECT avatar FROM users WHERE users.username = (?);'
    c.execute(getAva,(username,))
    ava = c.fetchall()
    return ava

'''
getDifficulty(username)
returns a an empty list if the user doesn't exist or if the user hasn't inputted any tasks.
returns a list of all the difficulties
'''
def getDifficulty(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    listDiff = 'SELECT difficulty FROM todo WHERE todo.username = (?);'
    c.execute(listDiff,(username,))
    diffList = c.fetchall()
    return diffList

'''
getTask(username)
returns a an empty list if the user doesn't exist or if the user hasn't inputted any tasks.
returns a list of all the tasks
'''
def getTask(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    listTasks = 'SELECT task FROM todo WHERE todo.username = (?);'
    c.execute(listTasks,(username,))
    taskList = c.fetchall()
    return taskList

def getCategory(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    listCategory = 'SELECT category FROM todo WHERE todo.username = (?);'
    c.execute(listCategory,(username,))
    categoryList = c.fetchall()
    return categoryList

'''
getPokemon(username)
returns a an empty list if the user doesn't exist or if the user hasn't obtained any pokemon
returns a list of all the pokemon
'''
def getPokemon(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    listPoke = 'SELECT cardID FROM pokemon WHERE pokemon.username = (?);'
    c.execute(listPoke,(username,))
    pokeList = c.fetchall()
    return pokeList

def getGold(username):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    listGold = 'SELECT gold FROM users WHERE users.username = (?);'
    c.execute(listGold,(username,))
    goldList = c.fetchall()
    return goldList

def entriesExist():
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    check = 'SELECT * FROM images;'
    c.execute(check)
    exist = c.fetchone()
    if exist is None:
        return False
    else:
        return True
