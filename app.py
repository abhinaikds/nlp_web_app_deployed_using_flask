from flask import Flask, render_template,request,redirect,session
from db import MyDb
import api

app=Flask(__name__)
app.secret_key = 'qwerty12345'
dbo=MyDb()

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/perform_registration',methods=["post"])
def perform_registration():
    name=request.form.get("user_name")
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    response=dbo.insert(name,email,password)
    if response==1:
        return render_template("login.html",message ="registration successful kindly login")
    else:
        return render_template("register.html",message ="email already exists")
    
@app.route('/perform_login',methods=["post"])
def perform_login():
    email=request.form.get("user_email")
    password=request.form.get("user_password")
    response=dbo.search(email,password)
    if response==1:
        session['logged_in']=1
        return redirect('/profile')
    else:
        return render_template("login.html",message ="incorrect email/password login with correct credentials again")

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=["post"])
def perform_ner():
    if session:
        text= request.form.get("ner_text")
        response=api.ner(text)
        return render_template("ner.html",response=response)
    else:
        return redirect('/')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Adjust the port as needed
