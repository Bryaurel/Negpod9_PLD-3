# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="root",
database = "negpod9"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "SELECT NAME, POINTSEARNED FROM DISPOSALHISTORY"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
