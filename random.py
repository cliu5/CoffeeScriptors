from flask import Flask,render_template,request,session,url_for,redirect,flash
import random
from os import urandom
import urllib
import pokemon as pokepy

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/",methods=['GET','POST'])
def ok():
    return render_template('random2.html')


@app.route("/gacha",methods=['GET','POST'])
def home():
    plist=pokepy.getAllPokemon()
    count=0
    while count<5:
        poke=random.choice(plist)
        if poke.getRarity=="Common":
            return render_template("random.html",
                                   pokemon=poke,
                                   img=img)
        if count>=1:
            if(poke.getRarity=="UnCommon"):
                return render_template("random.html",
                                       pokemon=poke,
                                       img=img)
        if count>=2:
            if poke.getRarity=="Rare":
                return render_template("random.html",
                                       pokemon=poke,
                                       img=img)



if __name__ == '__main__':
    app.debug = True
    app.run()
