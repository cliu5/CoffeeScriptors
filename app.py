from flask import Flask, render_template, request,session, url_for, redirect, flash
from os import urandom
from util import db_updater as update
from util import db_search as search
from util import db_builder as builder
from passlib.hash import sha256_crypt
import urllib
import json
import random
import pokemon as pokepy

import sqlite3 #imports sqlite
app = Flask(__name__)
app.secret_key = urandom(32)

#----------------------------------------------------------home--------------------------------------------------------
@app.route("/",methods=['GET','POST'])
def home():
    builder.main()
    if 'username' in session: #if user is logged in
        return redirect(url_for('authPage'))
    else:
        return render_template('auth.html')

#----------------------------------------------------------pick starter type--------------------------------------------
@app.route("/pick",methods=['GET','POST'])
def pick():
    return render_template('pick.html')

#----------------------------------------------------------receive starter----------------------------------------------
@app.route("/receive",methods=['GET','POST'])
def starter():
    if 'username' in session:
        username = session['username']
        whattype=request.form['type']
        if (whattype=='grass'):
            poke="Bulbasaur"
            img=pokepy.getImage("Bulbasaur")
            update.addpokemon(username,44)
        if (whattype=='fire'):
            poke="Charmander"
            img=pokepy.getImage("Charmander")
            update.addpokemon(username,46)
        if (whattype=='water'):
            poke="Squirtle"
            img=pokepy.getImage("Squirtle")
            update.addpokemon(username,63)
        update.updateavatar(username,poke)
        return render_template("pick2.html",
                                pokemon=poke,
                                pokeimg=img)
    else:
        return redirect(url_for('home'))
#----------------------------------------------------------gacha-------------------------------------------------------

@app.route("/gacha",methods=['GET','POST'])
def gacha():
    if 'username' in session:
        username=session['username']
        gold=search.getGold(username)[0][0]
        if gold>=100:
            update.updategold(username, gold, "subtract", 100)
            plist=pokepy.getAllPokemon()
            count=0
            while count<5:
                poke=random.choice(plist)
                if pokepy.getRarity(poke)=="Common":
                    update.addpokemon(username,pokepy.getID(poke)[6:])
                    return render_template("random.html",
                                           pokemon=poke,
                                           img=pokepy.getImage(poke))
                if count>=1:
                    if pokepy.getRarity(poke)=="Uncommon":
                        update.addpokemon(username,pokepy.getID(poke)[6:])
                        return render_template("random.html",
                                               pokemon=poke,
                                               img=pokepy.getImage(poke))
                if count>=2:
                    if pokepy.getRarity(poke)=="Rare":
                        update.addpokemon(username,pokepy.getID(poke)[6:])
                        return render_template("random.html",
                                               pokemon=poke,
                                               img=pokepy.getImage(poke))
        else:
            flash("Not enough gold")
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

#--------------------------------------------------login/register/logout-----------------------------------------------
@app.route("/logout")
def logout():
    '''
    Logs user out of session by popping them from the session. Returns user to log-in screen
    '''
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('authPage'))
    else:
        return redirect(url_for('home'))

@app.route("/auth",methods=['GET','POST'])
def authPage():
    '''
    Authenticates user signing in. Checks to see if password is correct or not;
    if correct, logs user in. If not, flashes "incorrect credentials"
    '''
    if 'username' in session:
        username = session['username']
        userNames = []
        tasks=search.getTask(username)
        difficulty=search.getDifficulty(username)
        category=search.getCategory(username)
        info = []
        for length in range(0, len(tasks)):
            row = []
            row.append((tasks[length])[0])
            row.append((difficulty[length])[0])
            row.append((category[length])[0])
            info.append(row)
        if search.getAvatar(username) ==[('',)]:
            return redirect(url_for('pick'))
        #if search.getTask(username)==[]:
            #return redirect(url_for('pick'))
        else:
            return render_template('home.html',
                                   avatar=pokepy.getImage(search.getAvatar(username)[0][0]),
                                   username = username,
                                   names = userNames,
                                   info = info)
    else:
        try:
            username=request.form['username'] #username
            password = search.password(username) #password that matches the username
            if password == None: #if credentials are incorrect
                flash('Wrong Username or Password!')
                return redirect(url_for('home')) #redirects
            elif sha256_crypt.verify(request.form['password'], password[0]): #if password is correct, login
                session['username'] = username
                return redirect(url_for('authPage'))
            else: #else credentials are wrong
                flash('Wrong Username or Password!')
                return redirect(url_for('home'))
        except:
            return redirect(url_for('home'))

@app.route("/reg",methods=['GET','POST'])
def reg():
    '''
    Loads the template that takes information and allows user to register,
    creating a new account that they can sign into session with
    '''
    if 'username' in session:
        return redirect(url_for('authPage'))
    return render_template('reg.html')

#--------------------------------------------------------database------------------------------------------------------
@app.route("/addTask",methods=['GET','POST'])
def addTask():
    if 'username' in session:
        return render_template('addTask.html')
    return redirect(url_for('home'))

@app.route("/deleteTask", methods=['GET','POST'])
def deleteTask():
    if 'username' not in session:
        flash("You need to be logged in to delete tasks.")
        return redirect('/auth')
    if 'username' in session:
        username=session['username']
        task = request.args.get("task")
        difficulty = search.getADiff(username, task)
        update.removetask(username,task)
        update.updategold(username, search.getGold(username), "add", difficulty *10)
    return redirect("/auth")


@app.route("/makeTask", methods=['GET','POST'])
def makeTask():
    if 'username' not in session:
        flash("You need to be logged in to add tasks.")
        return redirect('/auth')
    if 'username' in session:
        username=session['username']
    category = request.args.get("category")
    difficulty = request.args.get("difficulty")
    task=request.args.get('title')
    if category==None or task==None or difficulty==None:
        flash("You must fill in all parameters.")
        return redirect("/auth")
    update.addtask(username, difficulty, task, category)
    return redirect("/auth")

@app.route("/added",methods=['GET','POST'])
def added():
    '''
    Checks to see if username is unique,
    flashes "username taken" if it is,
    adds user and password to database if not and sends to home
    '''
    try:
        newUsername = request.form['username']
        newPassword = sha256_crypt.encrypt(request.form['password']) #encrypts password
        userList = search.username(newUsername)
        if userList == [] : #if username isn't taken
            update.adduser(newUsername,newPassword) #add to database
            return redirect(url_for('home'))
        else: #if username is taken
            flash('Username Taken')
            return redirect(url_for('reg'))
    except:
        return redirect(url_for('home'))

@app.route('/info')
def inventory():
    if 'username' in session:
        username = session['username']
        pokemon = []
        print(search.getPokemon(username))
        print(pokepy.getImage(13))
        for each in search.getPokemon(username):
            print(each[0])
            print(pokepy.getPokemon(each[0]))
            pokemon.append(pokepy.getImage(pokepy.getPokemon(each[0])))
        return render_template('inventory.html', pokeList = pokemon)
    else:
        return redirect(url_for('authPage'))

if __name__ == '__main__':
    app.debug = True
    app.run()
