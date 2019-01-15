''' this file stores the updating database code'''

import sqlite3
from flask import request,session
'''
adduser(username,password)
params:username, password
username is the username of the user
password is the password of the user
function adds the username and password to the users database
'''
def adduser(username, password):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO users VALUES(?,?,?,?)"
    params=(username,password,0,"")
    c.execute(insert,params)
    db.commit()
    db.close()

def addtask(username, difficulty, task, category): #adds a task to the todo list
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO todo VALUES(?,?,?,?)"
    params=(username,difficulty, task, category)
    c.execute(insert,params)
    db.commit()
    db.close()

def addpokemon(username, cardID):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO pokemon VALUES(?,?)"
    params=(username,cardID)
    c.execute(insert,params)
    db.commit()
    db.close()

def updateavatar(username, avatar):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "UPDATE users SET avatar=(?) WHERE username=(?);"
    params=(avatar,username)
    c.execute(insert,params)
    db.commit()
    db.close()

def updategold(username, original, operation, amount):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if operation=="subtract":
        gold=original-amount
    if operation=="add":
        gold=original+amount
    insert = "UPDATE users SET gold=(?) WHERE username=(?);"
    params=(gold,username)
    c.execute(insert,params)
    db.commit()
    db.close()

def removeuser(username, password):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "DELETE FROM users WHERE username=(?);"
    params=(username)
    c.execute(insert,params)
    db.commit()
    db.close()

def removetask(username, task): #adds a task to the todo list
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "DELETE FROM todo WHERE username=(?) and task=(?);"
    params=(username,task)
    c.execute(insert,params)
    db.commit()
    db.close()

def removepokemon(username, cardID):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "DELETE FROM users WHERE username=(?) and cardID=(?);"
    params=(username,cardID)
    c.execute(insert,params)
    db.commit()
    db.close()

def addimage(pokemon, url, rarity):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO images VALUES(?,?,?)"
    params=(pokemon,url,rarity)
    c.execute(insert,params)
    db.commit()
    db.close()
    
