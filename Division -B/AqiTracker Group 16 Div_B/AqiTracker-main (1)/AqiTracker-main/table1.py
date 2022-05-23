from prettytable import PrettyTable
from database import * 
# Specify the Column Names while initializing the Table


cursor.execute("SELECT * FROM aqi_data where City ='Mumbai'")
record = cursor.fetchall()
print("Total number of rows in table:", cursor.rowcount)
for row in record:
    myTable = PrettyTable("City" ,"Date" ,"AQI" , "Weather")
    myTable.add_row([row[0], row[1], row[2], row[3]])

 
print(myTable)