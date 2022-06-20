import mysql.connector
import os
import getpass
import base64

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

exitMenu=False
while not exitMenu:
	clearConsole()
	print()
	print("""
	-----------------------------

		Selecciona un idioma / Choose your language:

		1.ES
		2.EN
		3.Salir / Exit

	-----------------------------
	""")

	language=input("Opcion/option: ")

	if language=="3":
		clearConsole()
		exitMenu=True
	elif (language=="1") or (language=="2"):
		exitMenu=True
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


			def createUser():
				clearConsole()
				if language=="1":
					createNewUser=input("Nombre de usuario: ")
					createPassword=input("Contraseña: ")
					confirmPassword=input("Confirmar contraseña: ")

					if createPassword==confirmPassword:
						encryptPassword=base64.b64encode(createPassword.encode('utf-8'))
						insertNewUser="INSERT INTO user (user_name,user_password) values (%s,%s)"
						dbcursor.execute(insertNewUser,(createNewUser,encryptPassword))
						addNewUser=dbcursor.fetchall()
						dbConnection.commit()
						clearConsole()
					else:
						clearConsole()
						print("Contraseñas incorrectas, vuelve a intentarlo")
						createUSer()
				elif language=="2":
					createNewUser=input("Username: ")
					createPassword=input("Password: ")
					confirmPassword=input("Confirm password: ")

					if createPassword==confirmPassword:
						encryptPassword=base64.b64encode(createPassword.encode('utf-8'))
						insertNewUser="INSERT INTO user (user_name,user_password) values (%s,%s)"
						dbcursor.execute(insertNewUser,(createNewUser,encryptPassword))
						addNewUser=dbcursor.fetchall()
						dbConnection.commit()
						clearConsole()
					else:
						clearConsole()
						print("Invalid password, please try again")
						createUSer()

			def selectUser():
				clearConsole()
				if language=="1":
					selectUserName=input("Nombre de usuario: ")
					selectUserPassword=getpass.getpass("Contraseña: ")

					checkUser="SELECT * FROM user_id WHERE user_name=%s and user_password=%s"
					dbcursor.execute(checkUser,(selectUserName,selectUserPassword))
					verifyUser=dbcursor.fetchall()

					if verifyUser==True:
						pass
					else:
						print("ERROR")
						print("Usuario o contraseña incorrectos, vuelva a intentarlo")
						#hacer que el mensaje perdure unos segundos
						selectUser()
				elif language=="2":
					selectUserName=input("Username: ")
					selectUserPassword=getpass.getpass("Password: ")

					checkUser="SELECT * FROM user_id WHERE user_name=%s and user_password=%s"
					dbcursor.execute(checkUser,(selectUserName,selectUserPassword))
					verifyUser=dbcursor.fetchall()

					if verifyUser==True:
						pass
					else:
						print("ERROR")
						print("Password or Username invalid, please try again")
						#hacer que el mensaje perdure unos segundos
						selectUser()

			#def writeNewDream():

			#def editDream():

			#def showLastDream():

			#def showDreamByMonth():

			#def showDreamByYear():