from flask import Flask,render_template,request,session,url_for,redirect,flash
import random
from os import urandom
import urllib
import pokemon as pokepy

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/",methods=['GET','POST'])
def ok():
    return render_template('pick.html')

@app.route("/redone",methods=['GET','POST'])
def home():
    whattype=request.form['type']
    if (whattype=='grass'):
        poke="Bulbasaur"
        img=pokepy.getImage("Bulbasaur")
    if (whattype=='fire'):
        poke="Charmander"
        img=pokepy.getImage("Charmander")
    if (whattype=='water'):
        poke="Squirtle"
        img=pokepy.getImage("Squirtle")
    return render_template("pick2.html",
                           pokemon=poke,
                           pokeimg=img)

if __name__ == '__main__':
    app.debug = True
    app.run()
