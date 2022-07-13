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

		Selecciona un idioma / Choose your language:

			1.ES
			2.EN
			3.Salir / Exit

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

			def pressToContinue():
				conti=None
				if language=="1":
					conti=input("Pulse cualquier tecla para continuar")
				elif language=="2":
					conti=input("Press any key to continue")

				return conti

			def checkDelete():
				if language=="1":
					print("""\n 
						¿Esta seguro de querer continuar?
							1) Si
							2) No
					""")
					opt=None
					try:
						opt=int(input("Selecciona una opcion: "))
						if opt==1:
							return opt
						elif opt==2:
							pass
					except ValueError:
						print("ERROR, debes seleccionar el numero 1 o el 2")
						pressToContinue()
						clearConsole()

				elif language=="2":
					print("""\n 
						Do you want to continue?
							1) Yes
							2) No
					""")
					try:
						opt=int(input("Select an option: "))
						if opt==1:
							return opt
						elif opt==2:
							pass
					except ValueError:
						print("ERROR, you must between numbers 1 and 2")
						pressToContinue()
						clearConsole()
					return opt

			def showOption():
				opt=None
				if language=="1":
					try:
						opt=int(input("Selecciona una opcion: "))
					except ValueError:
						print("ERROR, debes seleccionar un numero del 1 al 5")
						pressToContinue()
						clearConsole()
					return opt
				elif language=="2":
					try:
						opt=int(input("Select an option: "))
					except ValueError:
						print("ERROR, you must choose a number between 1 to 5.")
						pressToContinue()
						clearConsole()
					return opt

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
						print("Se ha creado el usuario correctamente")
						pressToContinue()
						clearConsole()						
					else:
						clearConsole()
						print("Contraseñas incorrectas, vuelve a intentarlo")
						pressToContinue()
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
						print("The user has been created successfully")
						pressToContinue()
						clearConsole()						
					else:
						clearConsole()
						print("Invalid password, please try again")
						pressToContinue()
						createUSer()

				return addNewUser

			def selectUser():
				clearConsole()
				if language=="1":
					selectUserName=input("Nombre de usuario: ")
					selectUserPassword=getpass.getpass("Contraseña: ")

					checkUser="SELECT * FROM user_id WHERE user_name=%s and user_password=%s"
					dbcursor.execute(checkUser,(selectUserName,selectUserPassword))
					verifyUser=dbcursor.fetchall()

					if verifyUser==True:
						clearConsole()
					else:
						print("ERROR")
						print("Usuario o contraseña incorrectos, vuelva a intentarlo")
						pressToContinue()
						selectUser()

				elif language=="2":
					selectUserName=input("Username: ")
					selectUserPassword=getpass.getpass("Password: ")

					checkUser="SELECT * FROM user_id WHERE user_name=%s and user_password=%s"
					dbcursor.execute(checkUser,(selectUserName,selectUserPassword))
					verifyUser=dbcursor.fetchall()

					if verifyUser==True:
						clearConsole()
					else:
						print("ERROR")
						print("Password or Username invalid, please try again")
						pressToContinue()
						selectUser()

				return verifyUser

			def writeNewDream():
				clearConsole()
				if language=="1":
					print("Introduce la fecha del sueño: ")
					dreamYear=input("Año: ")
					dreamMonth=input("Mes: ")
					dreamDay=input("Día: ")
					dreamSummary=input("A continuación, relata el sueño: ")

					createNewDream="INSERT INTO dream (dream_year,dream_month,dream_day,dream_summary) values (%s,%s,%s,%s)"
					dbcursor.execute(createNewDream,(dreamYear,dreamMonth,dreamDay,dreamSummary))
					addNewDream=dbcursor.fetchall()
					dbConnection.commit()
					print("El sueño se ha registrado en la base de datos correctamente")
					pressToContinue()
					clearConsole()

				elif language=="2":
					print("Dream's date: ")
					dreamYear=input("Year: ")
					dreamMonth=input("Month: ")
					dreamDay=input("Day: ")
					dreamSummary=input("Now, write a summary about the dream: ")

					createNewDream="INSERT INTO dream (dream_year,dream_month,dream_day,dream_summary) values (%s,%s,%s,%s)"
					dbcursor.execute(createNewDream,(dreamYear,dreamMonth,dreamDay,dreamSummary))
					addNewDream=dbcursor.fetchall()
					dbConnection.commit()
					print("The dream has been registered in the database successfully")
					pressToContinue()
					clearConsole()

				return addNewDream

			def updateDream():
				clearConsole()
				updatedDream=None
				if language=="1":
					print("Introduce la fecha del sueño a editar: ")
					dreamYear=input("Año: ")
					dreamMonth=input("Mes: ")
					dreamDay=input("Día: ")
					print("""

						Selecciona que deseas editar: 

							1. Año
							2. Mes
							3. Día
							4. Resumen
							5. Salir

					""")
					updateDreamOption=input("Selecciona el número de la opción: ")
					if updateDreamOption=="1":
						newDreamYear=input("Introduce el año correcto del sueño: ")
						updateDreamYear="UPDATE dream SET dream_year=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamYear,(newDreamYear,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="2":
						newDreamMonth=input("Introduce el mes correcto del sueño: ")
						updateDreamMonth="UPDATE dream SET dream_month=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamMonth,(newDreamMonth,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="3":
						newDreamDay=input("Introduce el día correcto del sueño: ")
						updateDreamDay="UPDATE dream SET dream_day=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamDay,(newDreamDay,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="4":
						newDreamSummary=input("Introduce el resumen correcto del sueño: ")
						updateDreamSummary="UPDATE dream SET dream_summary=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamSummary,(newDreamSummary,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="5":
						clearConsole()
						pass
					
				elif language=="2":
					print("Write the date of the dream you want to edit: ")
					dreamYear=input("Year: ")
					dreamMonth=input("Month: ")
					dreamDay=input("Day: ")
			
					print("""

						What do you want to edit? Write the respective number below: 

							1. Year
							2. Month
							3. Day
							4. Summary
							5. Exit

					""")
					updateDreamOption=input("Write the number of the desired option: ")
					if updateDreamOption=="1":
						newDreamYear=input("Write the correct year of the dream: ")
						updateDreamYear="UPDATE dream SET dream_year=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamYear,(newDreamYear,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="2":
						newDreamMonth=input("Write the correct month of the dream: ")
						updateDreamMonth="UPDATE dream SET dream_month=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamMonth,(newDreamMonth,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="3":
						newDreamDay=input("Write the correct day of the dream: ")
						updateDreamDay="UPDATE dream SET dream_day=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamDay,(newDreamDay,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="4":
						newDreamSummary=input("Write the correct summary of the dream: ")
						updateDreamSummary="UPDATE dream SET dream_summary=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
						dbcursor.execute(updateDreamSummary,(newDreamSummary,dreamYear,dreamMonth,dreamDay))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="5":
						clearConsole()
						pass
				pressToContinue()
				clearConsole()
				return updatedDream

			def showLastDream():
				clearConsole()
				if language=="1":
					lastDream="SELECT * FROM dream ORDER BY dream_year DESC, dream_month DESC, dream_day DESC LIMIT 1"
					dbcursor.execute(lastDream)
					showLastDreamDetails=dbcursor.fetchall()

					for row in showLastDreamDetails:
						print('Fecha: ' + str(row[3]) + '-' + str(row[2]) + '-' + str(row[1]))
						print('Resumen del sueño: ' + row[4])

				elif language=="2":
					lastDream="SELECT * FROM dream ORDER BY dream_year DESC, dream_month DESC, dream_day DESC LIMIT 1"
					dbcursor.execute(lastDream)
					showLastDreamDetails=dbcursor.fetchall()

					for row in showLastDreamDetails:
						print('Date: ' + str(row[2]) + '-' + str(row[3]) + '-' + str(row[1]))
						print('Dream summary: ' + row[4])
					
				pressToContinue()
				clearConsole()
				return showLastDreamDetails

			def showDream():
				clearConsole()
				if language=="1":
					dreamYear=input("Introduce el año del sueño: ")
					dreamMonth=input("Introduce el mes del sueño: ")
					dreamDay=input("Introduce el día del sueño: ")
					selectedDream="SELECT * FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
					dbcursor.execute(selectedDream,(dreamYear,dreamMonth,dreamDay))
					showSelectedDream=dbcursor.fetchall()
					clearConsole()
					for row in showSelectedDream:
						print('Fecha: ' + str(row[3]) + '-' + str(row[2]) + '-' + str(row[1]))
						print('Resumen del sueño: ' + row[4])

				elif language=="2":
					dreamYear=input("Dream year: ")
					dreamMonth=input("Dream month: ")
					dreamDay=input("Dream day: ")
					selectedDream="SELECT * FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
					dbcursor.execute(selectedDream,(dreamYear,dreamMonth,dreamDay))
					showSelectedDream=dbcursor.fetchall()
					clearConsole()
					for row in showSelectedDream:
						print('Date: ' + str(row[2]) + '-' + str(row[3]) + '-' + str(row[1]))
						print('Dream summary: ' + row[4])
					
				pressToContinue()
				clearConsole()
				return showSelectedDream

			def deleteDream():
				clearConsole()
				deleteDreamReturn=None
				if language=="1":
					print("Introduce la fecha del sueño a eliminar")
					deleteYear=input("Año: ")
					deleteMonth=input("Mes: ")
					deleteDay=input("Día: ")
					deleteDreamQuery="DELETE FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
					checkOption=checkDelete()
					if checkOption==1:
						dbcursor.execute(deleteDreamQuery,(deleteYear,deleteMonth,deleteDay))
						deleteDreamReturn=dbcursor.fetchall()
						dbConnection.commit()
						print("El sueño se ha eliminado de la base de datos")
					elif checkOption==2:
						clearConsole()
						pass

				elif language=="2":
					print("Introduce the date of the dream to delete")
					deleteYear=input("Year: ")
					deleteMonth=input("Month: ")
					deleteDay=input("Day: ")
					deleteDreamQuery="DELETE FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s"
					checkOption=checkDelete()
					if checkOption==1:
						dbcursor.execute(deleteDreamQuery,(deleteYear,deleteMonth,deleteDay))
						deleteDreamReturn=dbcursor.fetchall()
						dbConnection.commit()
						print("The dream has been deleted from the database")
					elif checkOption==2:
						clearConsole()
						pass

				pressToContinue()
				clearConsole()
				return deleteDreamReturn

			exitMainMenu=False
			option=0

			while not exitMainMenu:	
				if language=="1":
					clearConsole()
					print("""

		Escoja una opcion:
			1) Escribir un nuevo sueño
			2) Actualizar un sueño ya existente
			3) Mostrar el último sueño
			4) Mostrar un sueño
			5) Borrar un sueños
			6) Salir

					""")
				elif language=="2":
					clearConsole()
					print("""

		Choose an option:
			1) Write a new dream
			2) Update a previous dream
			3) Show the last dream
			4) Show a dream
			5) Delete dream
			6) Exit

					""")
					
				option=showOption()

				if option==1:
					clearConsole()
					writeNewDream()
				if option==2:
					clearConsole()
					updateDream()
				if option==3:
					clearConsole()
					showLastDream()
				if option==4:
					clearConsole()
					showDream()
				if option==5:
					clearConsole()
					deleteDream()
				if option==6:
					clearConsole()
					exitMainMenu=True

