<html><head><style>body{
  max-width: 10px;
  padding: 10px;
  background-color: blue;
  position: fixed;
  top: 15px;
  left: 40px;

.form-container

{
  max-width: 900px;
  height: 600px;
  padding: 10px;
  background-color: Yellow;
  position: fixed;
  top: 50px;
  left: 500px;

  } 
        </style></head><body>
      <form  action="/login.py" method="post" class="form-container" >
                <label for="username"><b>USERNAME</b></label>
                <input type="text" placeholder="Enter username" name="username" required>
                <br>
                <label for="email"><b>Email</b></label>
                <input type="text" placeholder="Enter Email" name="email" required>
                <br>
                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw" required>
                <br>
                <label for="psw-repeat"><b>Repeat Password</b></label>
                <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
                <br>
                <button type ="button">Cancel</button>
                <div>
                <button  type="submit" value="submit">Sign Up</button>
                </div>



        	    {{ passwordmismatch }} 
                    {{  usernameexits  }}
                    {{ emailidexits  }}
                     

                </form>




       </body>
</html>

