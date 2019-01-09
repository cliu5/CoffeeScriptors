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
def adduser(username, password, pokemon,ID):
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO users VALUES(?,?,?,?,?)"
    params=(username,password,0,pokemon,ID)
    c.execute(insert,params)
    db.commit()
    db.close()

def addtask(username, difficulty, task): #adds a task to the todo list
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO todo VALUES(?,?,?)"
    params=(username, difficulty, task)
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
