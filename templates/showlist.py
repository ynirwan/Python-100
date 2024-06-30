<!doctype html>

	<html lang="en">
	  	</head>


	<body>
	   
	
{%for i in range(0, len)%} 


<li> <button style="width: 70px"; type="checkbox"  value="{{ todolist[i] }}">  {{ todolist[i] }}  </button> </li>


{%endfor%} 





            


     

  </body>

</html>