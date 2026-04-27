import  mysql
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "12345",
    use_pure = True
 )
cr = db.cursor()
cr.execute("show databases")
for i in cr:
    print(i)