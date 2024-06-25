
from flask import Flask, request, redirect 
import cgi, cgitb, validators, mariadb, sys

#class RegistrationForm():
   
 #   email = TextField('Email Address', [validators.Length(min=6, max=50)])
  # password = PasswordField('New Password', [
   #     validators.Required(),
    #    validators.EqualTo('confirm', message='Passwords must match')
   # ])
   # Password_repeat = PasswordField('Repeat Password')
   



app = Flask (__name__)

app.config["DEBUG"] = True
@app.route('/', methods=['GET'])

def home():
       header =  '<html><head> <title>Website</title> <style>body {background-color: Yellow; text-align: center;</style></head><body>'
       body =          '''<form  action="signup.html">
                          <button type="submit">Sign Up</button>
                          </form>
                          <h1 style="text-align:center;">  <b>To Do list</b>  </h1>
                          <p  style="text-align:center;">Start Your Day With Us</p>
                         <form action="login.php">
                        
                         <input type="Username"  size="10" placeholder="Please input your name" required>
                         <input type="Password"  size="10" placeholder="Input Password" required>
                        
    
                         <div>
                         <input type="submit" value="submit">
                         </div>
                         </form>'''
       footer =  '</body></html>'
       return header + body + footer



@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
       
       header = '<html><head><style>body{background-color: Yellow; text-align: center;</style></head><body>'
       body = '''<form  action="/data.html" method="post">
                <label for="email"><b>Email</b></label>
                <input type="text" placeholder="Enter Email" name="email" required>
                <br>
                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw" required>
                <br>
                <label for="psw-repeat"><b>Repeat Password</b></label>
                <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
                <br>
                <button typ ="button">Cancel</button>
                <div>
                <button  type="submit" value="submit">Sign Up</button>
                </div>
                </form>'''
       footer = '</body></html>'
       return header + body + footer
 
  




@app.route('/data.html', methods=['GET', 'POST'])
def hello():
       if request.method == 'POST': #this block is only entered when the form is submitted
          email = request.form.get('email')
          psw = request.form['psw']

          #return '<h1>The Email value is: {}</h1>
           #       <h1>The password value is: {}</h1>'.format(email, psw)
       return redirect("/")










if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

 
