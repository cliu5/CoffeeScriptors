import sqlite3 #imports sqlite

def users(): #creates the users db
    DB_FILE="data/CoffeeScriptors.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT, gold INTEGER, avatar TEXT)" #user table
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS todo(username TEXT, difficulty INTEGER, task TEXT, category TEXT)" #to-do list table
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS pokemon(username TEXT, cardID TEXT)" #pokemon table
    command = "CREATE TABLE IF NOT EXISTS pictures(cardID TEXT, picture BLOB)"
    c.execute(command)
    db.commit()
    db.close()
    
def main(): #calls all of the functions to build the databases
    try:
        users()
    except:
        pass

