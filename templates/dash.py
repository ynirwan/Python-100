<!doctype html>

	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	<style>
	 .container .btn {
	   position: absolute;
	   top: 50%;
	   left: 5%;
	   transform: translate(-50%, -50%);
	   -ms-transform: translate(-50%, -50%);
	   background-color: #555;
	   color: white;
	   font-size: 16px;
	   padding: 5px 5px;
	   border: none;
	   cursor: pointer;
	   border-radius: 5px;
	 }
	</style>
	</head>


	<body>
	   

	   
	    
	    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
	    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
	     <nav class="navbar navbar-dark fixed-top bg-primary flex-md-nowrap p-0 shadow"> 
	     <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#"> Dashboard</a>
	     <ul class="navbar-nav px-5">
	<li class="nav-item text-nowrap">



     <b>HI</b> <button type="button"> {{ username }} </button>
     
     <a class="nav-link" href="#">Logout</a>
    </li>
    </ul>
    </nav>
       
       <div> 
         <a  href="todolist.html">
         <img src="{{url_for('static', filename='todolist.jpg')}}" style="width:300px;height:300px;" />
         <button class="btn">  TODO  </button> 
       </div>    
     


     






  </body>

</html>





