import sqlite3 #imports sqlite

def users(): #creates the users db
    DB_FILE="./data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE users(username TEXT, password TEXT, gold INTEGER, avatar TEXT, INTEGER PRIMARY KEY (ID))" #user table
    c.execute(command)
    command = "CREATE TABLE todo(username TEXT, difficulty INTEGER, task TEXT)" #to-do list table
    c.execute(command)
    command = "CREATE TABLE pokemon(username TEXT, cardID TEXT)" #pokemon table
    c.execute(command)

def main(): #calls all of the functions to build the databases
    try:
        users()
    except:
        pass
