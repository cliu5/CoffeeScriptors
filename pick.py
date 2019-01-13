from flask import Flask,render_template,request,session,url_for,redirect,flash
import random
from os import urandom
import urllib

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/",methods=['GET','POST'])
def ok():
    return render_template('pick.html')

@app.route("/redone",methods=['GET','POST'])
def home():
    whattype=request.form['type']
    if (whattype=='grass'):
        poke="bulbasaur"
    if (whattype=='fire'):
        poke="charmander"
    if (whattype=='water'):
        poke="squirtle"
    return render_template("pick2.html",
                           pokemon=poke)

if __name__ == '__main__':
    app.debug = True
    app.run()
