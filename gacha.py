from flask import Flask,render_template,request,session,url_for,redirect,flash
import random
from os import urandom
import urllib
import pokemon as pokepy
from util import db_search as search
from util import db_updater as update

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/",methods=['GET','POST'])
def ok():
    return render_template('random2.html')


@app.route("/gacha",methods=['GET','POST'])
def home():
    if search.entriesExist() == False:
        plist=pokepy.getAllPokemon()
        for poke in plist:
            update.addimage(poke, pokepy.getImage(poke), getRarity(poke))
        count=0
        while count<5:
            poke=random.choice(plist)
            if pokepy.getRarity(poke)=="Common":
                return render_template("random.html",
                                   pokemon=poke,
                                   img=pokepy.getImage(poke))
            if count>=1:
                if pokepy.getRarity(poke)=="UnCommon":
                    return render_template("random.html",
                                           pokemon=poke,
                                           img=pokepy.getImage(poke))
            if count>=2:
                if pokepy.getRarity(poke)=="Rare":
                return render_template("random.html",
                                       pokemon=poke,
                                       img=pokepy.getImage(poke))



if __name__ == '__main__':
    app.debug = True
    app.run()
