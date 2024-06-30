from flask import Flask, request, redirect, Response, render_template, flash, session 
import cgi, cgitb, validators, sys, redis,  pymongo
from datetime import date 
import os, re, socket 
from werkzeug.utils import secure_filename


myclient = pymongo.MongoClient("mongodb://mongo:27017/")
mydb = myclient["customers"]
mydb1 = myclient["eMAIL"]
emailcoll = mydb1["Emailcollection"]




SIGNUP = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)


app = Flask (__name__)
app.secret_key = "f9bf78b9a18ce6d46a0cd2b0b86df9dai"


app.config["DEBUG"] = True
@app.route('/', methods=['GET', 'POST'])

def home():
       return render_template("index.html")

@app.route('/signup.py', methods=['GET', 'POST'])
def signup():
       
           return render_template("/signup.py")





@app.route('/login.py', methods=['GET', 'POST'])
def login():
          usernameexits= "ussername exits"
          emailidexits=  "Email id exits"
          passwordmismatch="Password MismatCh"
          username = request.form.get('username')
          email = request.form.get('email')
          psw = request.form.get('psw')
          repsw = request.form.get('psw-repeat')
   

          if psw != repsw :
           return render_template("/signup.py", passwordmismatch=passwordmismatch)  

          e = None 

        
          r  =   SIGNUP.hget(username, 'EMAIL')
          mydict1 = ({"EMAIL": email})
        
          mydoc = emailcoll.find_one(mydict1)
         

          if r != e:
            return render_template("/signup.py", usernameexits=usernameexits)
          elif mydoc != e:
            return render_template("/signup.py", emailidexits=emailidexits)
          else:
                SIGNUP.lpush(username+"todolist", "list1")
                SIGNUP.hmset(username, {'EMAIL': email, 'PASSWORD': psw})
                myclient = pymongo.MongoClient("mongodb://mongo:27017/")
                mydb = myclient["customers"]
                mycol = mydb[ ( username ) ] 
                mydict = { "NAME":  "username" , "EMAIL": "EMAIL" }
                mydict["NAME"] = username
                mydict["EMAIL"] = email
                x = emailcoll.insert_one(mydict1)
                x = mycol.insert_one(mydict)
                return render_template("login.py", username=username)

 
         




@app.route('/dash.py', methods=['GET', 'POST'])
def dash():
        
          loginsuccess= "You were successfully logged in"
          loginfail= "CheCk your Credentials"

          username = request.form.get('username')
          password = request.form.get('password')
          Access  =   SIGNUP.hget(username, 'PASSWORD')
          session['username']= username;

          if Access == password : 
           return render_template("dash.py", username=username,loginsuccess=loginsuccess)
          else:
          
           return render_template("/index.html", loginfail=loginfail)


@app.route('/todolist.html', methods=['GET', 'POST'])
def todolist():
          username =  session['username'];

          todolist = SIGNUP.lrange(username+"todolist",  0, -1)

          return render_template("todolist.html",  len = len(todolist), todolist = todolist)


@app.route('/create.py', methods =['POST', 'GET'])
def  create():

          username =  session['username'];
          todolist = SIGNUP.lrange(username+"todolist",  0, -1)
          listexits=  "listexits"
          name = str(request.form.get('Name'))
          item1 = str(request.form.get('ITEM1'))
          item2 = str(request.form.get('ITEM2'))
          item3 = str(request.form.get('ITEM3'))
          item4 = str(request.form.get('ITEM4'))
          item5 = str(request.form.get('ITEM5'))
          u = username+"todolist"
          p1 = "'{}'".format(u)
          p4 = str(u)

          r  =   SIGNUP.lrange(p4, 0, -1)

          if name in r:
                    
           return render_template("/todolist.html",  listexits=listexits,  len = len(todolist), todolist=todolist) 
                   
          else: 


           SIGNUP.lpush(p4,  name)
           SIGNUP.lpush(username+name, item1, item2, item3, item4, item5)

           return redirect("todolist.html")

          
 
      #    return render_template("print.html",  r = item4, name=name )



@app.route('/showlist.py', methods =['POST', 'GET'])
def  show():

          username =  session['username'];
          name = str(request.form.get('name'))
          u = username+name
          p1 = "'{}'".format(u)
          p4 = str(u)
          todolist = SIGNUP.lrange(p4,   0, -1)


          return render_template("showlist.py",   len = len(todolist),todolist = todolist)

        


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 


