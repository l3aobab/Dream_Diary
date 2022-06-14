import mysql.connector
import os
import getpass
import base64

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

print()
print("""
-----------------------------

	1.ES
	2.EN

-----------------------------
""")

language=int(input("Selecciona un idioma / Choose your language: "))

dbConnection=mysql.connector.connect(host="localhost",user="root",password='abc123.')
dbcursor=dbConnection.cursor()
clearConsole()

if dbConnection:
	createDataBase="CREATE DATABASE IF NOT EXISTS DreamDiary"
	useDataBase="USE DreamDiary"
	createUserTable="CREATE TABLE IF NOT EXISTS user (user_id int PRIMARY KEY AUTO_INCREMENT,user_name varchar(256) NOT NULL,user_password varchar(256) NOT NULL)"
	createDreamTable="CREATE TABLE IF NOT EXISTS dream (dream_code int PRIMARY KEY AUTO_INCREMENT,dream_year int NOT NULL,dream_month varchar(20) NOT NULL,dream_day int NOT NULL,dream_summary varchar(5000) NOT NULL)"

	dbcursor.execute(createDataBase)
	dbcursor.execute(useDataBase)
	dbcursor.execute(createUserTable)
	dbcursor.execute(createDreamTable)	


	#def createUser:

	#def selectUser:

	#def writeNewDream:

	#def editDream:

	#def showLastDream:

	#def showDreamByMonth:

	#def showDreamByYear: