import mysql.connector
mydb = mysql.connector.connect(
    host=172.17.0.4,
    user=root,
    password=some_password
)
