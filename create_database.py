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

# creating table
DisposalHistory = """CREATE TABLE DISPOSALHISTORY (
				NAME VARCHAR(50) NOT NULL,
				DISPOSALDATE DATE NOT NULL,
				WASTETYPE VARCHAR(50) NOT NULL,
				WASTEWEIGHT INT NOT NULL,
				POINTSEARNED INT
				)"""

# table created
cursorObject.execute(DisposalHistory)

# disconnecting from server
dataBase.close()

