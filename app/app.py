from flask import Flask, request, redirect, Response, render_template, flash, session 
import cgi, cgitb, validators, sys, redis,  pymongo
from datetime import date 
import os, re, socket 
from werkzeug.utils import secure_filename


myclient = pymongo.MongoClient("mongodb://mongo:27017/")
mydb = myclient["customers"]
mydb1 = myclient["eMAIL"]
emailcoll = mydb1["Emailcollection"]

UPLOAD_FOLDER = 'uploads'



SIGNUP = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)


app = Flask (__name__)
app.secret_key = "f9bf78b9a18ce6d46a0cd2b0b86df9dai"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config["DEBUG"] = True
@app.route('/', methods=['GET', 'POST'])

def home():
       return render_template("index.html")

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
       
       return render_template("signup.html")
 
 
@app.route('/login.py', methods=['GET', 'POST'])
def login():
          usernameexits= "ussername exits"
          emailidexits=  "Email id exits"
          passwordmismatch="Password MismatCh"
          username = request.form.get('username')
          email = request.form.get('email')
          psw = request.form['psw']
          repsw = request.form['psw-repeat']
   

          if psw != repsw :
           return render_template("/signup.html", passwordmismatch=passwordmismatch)  

          e = None 

        
          r  =   SIGNUP.hget(username, 'EMAIL')
          mydict1 = ({"EMAIl": email})
        
          mydoc = emailcoll.find_one(mydict1)
         

          if r != e:
            return render_template("/signup.html", usernameexits=usernameexits)
          elif mydoc != e:
            return render_template("/signup.html", emailidexits=emailidexits)
          else:
                SIGNUP.lpush(username+"todolist", "list1")
                SIGNUP.hmset(username, { 'EMAIL' : email, 'PASSWORD' : psw })
                myclient = pymongo.MongoClient("mongodb://mongo:27017/")
                mydb = myclient["customers"]
                mycol = mydb[ ( username ) ] 
                mydict = { "NAME":  "username" , "EMAIL": "EMAIL" }
                mydict["NAME"] = username
                mydict["EMAIL"] = email
                x = emailcoll.insert_one(mydict1)
                x = mycol.insert_one(mydict)
                fin = open("adduserrun.yaml", "rt")
                data = fin.read()
                data = data.replace('root', username)
                data = data.replace('test', psw)
                fin.close()
                fin = open("adduserrun.yaml", "wt")
                fin.write(data)
                fin.close()
                text = os.system('ansible-playbook adduserrun.yaml >> sample.txt') 
                os.system('cp adduser.yaml  adduserrun.yaml')
                return render_template("login.html", username=username)

 
         




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
   
          return render_template("todolist.html",  todolist = todolist) 

@app.route('/show.html', methods= ['GET', 'POST'])
def show():
          username =  session['username'];
          listname =   str(request.form.get('listname'))
          x =  SIGNUP.lrange(username+listname, 0, -1)
          x.reverse() 
          return render_template("todolist.html", x=x) 

@app.route('/create.py', methods =['POST', 'GET'])
def  create():
          
          username =  session['username'];          
          name = str(request.form.get('Name'))
          item1 = str(request.form.get('ITEM1'))
          item2 = str(request.form.get('ITEM2'))
          item3 = str(request.form.get('ITEM3'))
          item4 = str(request.form.get('ITEM4'))
          item5 = str(request.form.get('ITEM5'))
          u = username+"todolist"
          p1 = "'{}'".format(u)
          p4 = str(u)
          SIGNUP.lpush(p4,  name) 
          SIGNUP.lpush(username+name, item1, item2, item3, item4, item5)
          username =  session['username'];
          return redirect("todolist.html",) 


@app.route('/ansible.html', methods=['GET', 'POST'])
def ansible():
          username =  session['username'];
          node = SIGNUP.lrange(username+"node",  0, -1)

          return render_template("ansible.html",username=username,node=node)




@app.route('/ssh.py', methods=['GET', 'POST'])
def ssh():
          username =  session['username'];
          name = str(request.form.get('name'))
          ipaddress = str(request.form.get('ip'))
          port = str(request.form.get('port'))
          password = str(request.form.get('password'))
            
         
          fin = open("ansiblessh.yaml", "rt")
          data = fin.read()
          data = data.replace('root', name)
          data = data.replace('127.0.0.0', ipaddress)
          data = data.replace('22', port)
          data = data.replace('password', password)
          fin.close()
          fin = open("ansiblessh.yaml", "wt")
          fin.write(data)
          fin.close()
          os.system('cp ansibless.yaml  ansiblessh.yaml')
           

          return render_template("ansible.html",username=username)
   

           
@app.route('/add.py', methods=['GET', 'POST'])
def add():
         username =  session['username'];
         Node  = str(request.form.get('Name'))
         Port  = str(request.form.get('Port'))
         user = str(request.form.get('username'))
         IP  = str(request.form.get('ip'))
        

         SIGNUP.hmset(username+"node"+Node, { 'Port' : Port, 'IP' : IP, 'username' : user })
         u = username+"node"
         p1 = "'{}'".format(u)
         p4 = str(u)
         SIGNUP.lpush(p4,  Node)
         return render_template("ansible.html")


@app.route('/view.py', methods = ['get', 'post' ])
def view():
         username =  session['username'];
         todolist = SIGNUP.lrange(username+"node",  0, -1)
         return render_template("ansible.html")
                   

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded successfully'




@app.route('/listname.py', methods=['GET', 'POST'])
def listname():
          return render_template("todolist.html")

@app.route("/flash")
def flash():
    flash("This is a flashed message.")
    return render_template("flash.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

 
