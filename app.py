from flask import Flask, request, redirect, Response, render_template, flash 
import cgi, cgitb, validators, sys, redis,  pymongo
from datetime import date 




myclient = pymongo.MongoClient("mongodb://172.18.0.4:27017/")
mydb = myclient["customers"]
mydb1 = myclient["eMAIL"]
emailcoll = mydb1["Emailcollection"]





SIGNUP = redis.Redis(host='redis', port=6379, db=0)


app = Flask (__name__)

app.config["DEBUG"] = True
@app.route('/', methods=['GET', 'POST'])

def home():
       return render_template("index.html")



@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
       
       return render_template("signup.html")
 
 
@app.route('/login.py', methods=['GET', 'POST'])
def login():

          username = request.form.get('username')
          email = request.form.get('email')
          psw = request.form['psw']
          repsw = request.form['psw-repeat']
   

          if psw != repsw :
          # flash('You were successfully logged in')
           return redirect("/signup.html")  

          e = None 

        
          r  =   SIGNUP.hget(username, 'EMAIL')
          mydict1 = ({"EMAIl": email})
        
          mydoc = emailcoll.find_one(mydict1)
         

          if r != e:
            return redirect("/signup.html")
          elif mydoc != e:
            return redirect("/signup.html")
          else:
           SIGNUP.hmset(username, { 'EMAIL' : email, 'PASSWORD' : psw })
           myclient = pymongo.MongoClient("mongodb://172.18.0.4:27017/")
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


          username = request.form.get('username')
          password = request.form.get('password')
          Access  =   SIGNUP.hget(username, 'PASSWORD')
          A  = str(Access)
          p = password
          p1 = "'{}'".format(p)
          r1 =   str("b")+ p1
          Access1 = str(r1)


          if Access1 == A : 
           return render_template("dash.py", username=username)
          else:
           return render_template("signup.html")
            



























@app.route('/todolist.html', methods=['GET', 'POST'])
def todolist():
          today = date.today()
         
          return render_template("todolist.html", today=today) 

@app.route('/create.py', methods =['POST', 'GET'])
def  create():
          today = date.today() 
          return render_template("/create.py", today=today) 

@app.route('/listdate.py', methods=['GET', 'POST'])
def listdate():
          return render_template("todolist.html")

@app.route('/listname.py', methods=['GET', 'POST'])
def listname():
          return render_template("todolist.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

 
