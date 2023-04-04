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

sql = "INSERT INTO DISPOSALHISTORY (NAME, DISPOSALDATE, WASTETYPE, WASTEWEIGHT, POINTSEARNED)\
VALUES (%s, %s, %s, %s, %s)"
val = [("Cynthia", "2023-11-04", "Plastic Waste", "5", "100"),
       ("Islam", "2023-09-04", "Glassware Waste", "10", "80"),
       ("Ange", "2023-05-04", "E-Waste", "30", "200"),
       ("Nina", "2023-13-04", "Organic Waste", "15", "150"),
       ("Kur", "2023-06-04", "Glassware Waste", "40", "167"),
       ("Maxime", "2023-01-05", "Organic Waste", "25", "185"),
       ("Bryan", "2023-02-03", "Plastic Waste", "21", "280"),
       ("Tesfahun", "2023-19-02", "Plastic Waste", "8", "155"),
       ("Julliet", "2023-10-04", "Plastic Waste", "16", "225"),
       ("Annet", "2023-07-03", "Organic Waste", "33", "300")]
 
   
cursorObject.executemany(sql, val)
dataBase.commit()
   
# disconnecting from server
dataBase.close()