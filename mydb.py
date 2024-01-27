import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'Unuttunmu1.'

	)

#prepapre a cursor obj

cursorObject = dataBase.cursor()

#Create Database

cursorObject.execute("CREATE DATABASE ekinoks")

print("Engaged!")