from flask import Flask,render_template,request,session,url_for,redirect,flash
import random
import urllib

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def ok():
    return render_template('pick.html')

@app.route("/redone",methods=['GET','POST'])
def home():
    whattype=request.form['type']
    flash(whattype)
    return redirect(url_for("ok"))

if __name__ == '__main__':
    app.debug = True
    app.run()
