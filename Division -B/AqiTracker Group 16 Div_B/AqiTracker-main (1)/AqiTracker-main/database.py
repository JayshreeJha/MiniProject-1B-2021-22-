import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='aqi_data',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        
        cursor.execute("select * from aqi_data where City = 'Delhi'")
        record = cursor.fetchall()
        # print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e) 
finally:
    if connection.is_connected():
        # cursor.close()
        # connection.close()
        print("u done")
