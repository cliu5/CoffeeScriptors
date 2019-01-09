import sqlite3 #imports sqlite

def users(): #creates the users db
    DB_FILE="./data/CoffeeScriptors.db" 
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE users(username TEXT, password TEXT, score INTEGER)"
    c.execute(command)


def main(): #calls all of the functions to build the databases
    try:
        
        users()
        questions()
    except:
        pass
