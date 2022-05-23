import _mysql_connector
import mysql.connector

HOST="localhost"
PORT="3306"
USER="spaceinvader"
PASSWORD="si123"
DB="spaceinvader"

db=mysql.connector.Connect(host=HOST,port=PORT,user=USER,passwd=PASSWORD,db=DB)
print("success")
print("Connection Successful to", HOST)
dbhandler=db.cursor()
print("Cursor selected")

dbhandler.execute("SELECT * from marks")
print("Query execute")
result=dbhandler.fetchall()

db.close()