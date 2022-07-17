import mysql.connector
import os
import getpass
import base64

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

def pressToContinue():
	conti=None
	if language=="1":
		conti=input("Pulse cualquier tecla para continuar")
	elif language=="2":
		conti=input("Press any key to continue")

	return conti

def showOption():
	opt=None
	if language=="1":
		try:
			opt=int(input("Selecciona una opcion: "))
		except ValueError:
			print("ERROR, debes seleccionar un numero")
			pressToContinue()
			clearConsole()
		return opt
	elif language=="2":
		try:
			opt=int(input("Select an option: "))
		except ValueError:
			print("ERROR, you must choose a number")
			pressToContinue()
			clearConsole()
		return opt

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
		clearConsole()
		#IMPORTANTE ESTO DE AQUI, TIENE QUE ESTAR EN TRUE PARA QUE NO SE QUEDE EN UN BUCLE
		exitMenu=True
		userName=None
		userPass=None
		ddbbIP=None
		dbConnection=None
		exitSubMenu=False

		#testear
		def createUser():
			clearConsole()
			if language=="1":
				newUserName=input("Nombre de usurio: ")
				newUserPass=getpass.getpass("Contraseña: ")
				confirmNewUserPass=getpass.getpass("Confirmar contraseña: ")
				newUserDdbbIP=input("IP de la base de datos: ")
				if newUserPass==confirmNewUserPass:
					#crear un usuario especifico para esto solo con grant create
					tempConnection=mysql.connector.connect(host=newUserDdbbIP,user="root",password="abc123.")
					tempCursor=tempConnection.cursor()
					#si no va ponerle comilla simple a las s
					createUserQuery="CREATE USER %s@%S IDENTIFIED BY %s"
					tempCursor.execute(createUserQuery,(newUserName,newUserDdbbIP,newUserPass))

					grantSelect="GRANT SELECT ON DreamDiary.dream FROM %s@%s"
					grantUpdate="GRANT UPDATE ON DreamDiary.dream FROM %s@%s"
					grantDelete="GRANT DELETE ON DreamDiary.dream FROM %s@%s"

					tempCursor.execute(grantSelect,(newUserName,newUserDdbbIP))
					tempCursor.execute(grantUpdate,(newUserName,newUserDdbbIP))
					tempCursor.execute(grantDelete,(newUserName,newUserDdbbIP))
					tempCursor.execute("Flush Privileges")

					tempCursor.close()
					tempConnection.close()
			elif language=="2":
				newUserName=input("Username: ")
				newUserPass=getpass.getpass("Password: ")
				confirmNewUserPass=getpass.getpass("Confirm password: ")
				newUserDdbbIP=input("Database IP: ")
				if newUserPass==confirmNewUserPass:
					#crear un usuario especifico para esto solo con grant create
					tempConnection=mysql.connector.connect(host=newUserDdbbIP,user="root",password="abc123.")
					tempCursor=tempConnection.cursor()
					#si no va ponerle comilla simple a las s
					createUserQuery="CREATE USER %s@%S IDENTIFIED BY %s"
					tempCursor.execute(createUserQuery,(newUserName,newUserDdbbIP,newUserPass))

					grantSelect="GRANT SELECT ON DreamDiary.dream FROM %s@%s"
					grantUpdate="GRANT UPDATE ON DreamDiary.dream FROM %s@%s"
					grantDelete="GRANT DELETE ON DreamDiary.dream FROM %s@%s"

					tempCursor.execute(grantSelect,(newUserName,newUserDdbbIP))
					tempCursor.execute(grantUpdate,(newUserName,newUserDdbbIP))
					tempCursor.execute(grantDelete,(newUserName,newUserDdbbIP))
					tempCursor.execute("Flush Privileges")

					tempCursor.close()
					tempConnection.close()
			pressToContinue()
			clearConsole()
			return newUser

		if language=="1":
			while not exitSubMenu:
				print("""
					Seleccione una opcion:
						1) Iniciar sesion
						2) Crear usuario	
				""")
				subMenuOption=showOption()

				if subMenuOption==1:
					clearConsole()
					userName=input("Nombre de usuario: ")
					userPass=getpass.getpass("Contraseña:")
					ddbbIP=input("IP de la base de datos: ")
					exitSubMenu=True
				elif subMenuOption==2:
					clearConsole()
					createUSer()

		elif language=="2":
			userName=input("Username: ")
			userPass=getpass.getpass("Password: ")
			ddbbIP=input("Database IP: ")

		dbConnection=mysql.connector.connect(host=ddbbIP,user=userName,password=userPass)
		dbcursor=dbConnection.cursor()
		clearConsole()

		if dbConnection:
			createDataBase="CREATE DATABASE IF NOT EXISTS DreamDiary"
			useDataBase="USE DreamDiary"

			createUserTable="""
			CREATE TABLE IF NOT EXISTS user (
				id int AUTO_INCREMENT,
				user_name varchar(50) NOT NULL,
				user_password varchar(256) NOT NULL,
				PRIMARY KEY (id,user_name))"""

			createDreamTable="""
			CREATE TABLE IF NOT EXISTS dream (
				code int AUTO_INCREMENT,
				dream_year int NOT NULL,
				dream_month varchar(20) NOT NULL,
				dream_day int NOT NULL,
				dream_title varchar(75) NOT NULL,
				dream_summary varchar(5000) NOT NULL,
				dream_user_name varchar(50),
				PRIMARY KEY (code,dream_title))"""

			dbcursor.execute(createDataBase)
			dbcursor.execute(useDataBase)
			dbcursor.execute(createUserTable)
			dbcursor.execute(createDreamTable)

			

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

			#revisar en el futuro
			def insertUserAdmin():
				clearConsole()
				if language=="1":
					createNewUser=input("Nombre de usuario: ")
					createPassword=getpass.getpass("Contraseña: ")
					confirmPassword=getpass.getpass("Confirmar contraseña: ")

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
					createPassword=getpass.getpass("Password: ")
					confirmPassword=getpass.getpass("Confirm password: ")

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

			def writeNewDream():
				clearConsole()
				if language=="1":
					print("Introduce la fecha del sueño: ")
					dreamYear=input("Año: ")
					dreamMonth=input("Mes: ")
					dreamDay=input("Día: ")
					dreamTitle=input("Titulo: ")
					dreamSummary=input("A continuación, relata el sueño: ")

					createNewDream="INSERT INTO dream (dream_year,dream_month,dream_day,dream_title,dream_summary,dream_user_name) VALUES (%s,%s,%s,%s,%s,%s)"
					dbcursor.execute(createNewDream,(dreamYear,dreamMonth,dreamDay,dreamTitle,dreamSummary,userName,))
					addNewDream=dbcursor.fetchall()
					dbConnection.commit()

					print("\nEl sueño se ha registrado en la base de datos correctamente")
					pressToContinue()
					clearConsole()

				elif language=="2":
					print("Dream's date: ")
					dreamYear=input("Year: ")
					dreamMonth=input("Month: ")
					dreamDay=input("Day: ")
					dreamTitle=input("Title: ")
					dreamSummary=input("Now, write a summary about the dream: ")

					createNewDream="INSERT INTO dream (dream_year,dream_month,dream_day,dream_title,dream_summary,dream_user_name) VALUES (%s,%s,%s,%s,%s,%s)"
					dbcursor.execute(createNewDream,(dreamYear,dreamMonth,dreamDay,dreamTitle,dreamSummary,userName,))
					addNewDream=dbcursor.fetchall()
					dbConnection.commit()

					print("\nThe dream has been registered in the database successfully")
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
							4. Titulo
							5. Resumen
							6. Salir

					""")
					updateDreamOption=input("Selecciona el número de la opción: ")
					if updateDreamOption=="1":
						newDreamYear=input("Introduce el año correcto del sueño: ")
						updateDreamYear="UPDATE dream SET dream_year=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamYear,(newDreamYear,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="2":
						newDreamMonth=input("Introduce el mes correcto del sueño: ")
						updateDreamMonth="UPDATE dream SET dream_month=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamMonth,(newDreamMonth,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="3":
						newDreamDay=input("Introduce el día correcto del sueño: ")
						updateDreamDay="UPDATE dream SET dream_day=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamDay,(newDreamDay,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="4":
						newDreamTitle=input("Introduce el titulo correcto del sueño: ")
						updateDreamDay="UPDATE dream SET dream_title=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamTitle,(newDreamDay,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="5":
						newDreamSummary=input("Introduce el resumen correcto del sueño: ")
						updateDreamSummary="UPDATE dream SET dream_summary=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamSummary,(newDreamSummary,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="6":
						clearConsole()
						pass
					print("Se ha actualizado correctamente el sueño")
					
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
							4. Title
							5. Summary
							6. Exit

					""")
					updateDreamOption=input("Write the number of the desired option: ")
					if updateDreamOption=="1":
						newDreamYear=input("Write the right year of the dream: ")
						updateDreamYear="UPDATE dream SET dream_year=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamYear,(newDreamYear,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="2":
						newDreamMonth=input("Write the right month of the dream: ")
						updateDreamMonth="UPDATE dream SET dream_month=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamMonth,(newDreamMonth,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="3":
						newDreamDay=input("Write the right day of the dream: ")
						updateDreamDay="UPDATE dream SET dream_day=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamDay,(newDreamDay,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="4":
						newDreamTitle=input("Write the right title of the dream: ")
						updateDreamDay="UPDATE dream SET dream_title=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamTitle,(newDreamDay,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="5":
						newDreamSummary=input("Write the right summary of the dream: ")
						updateDreamSummary="UPDATE dream SET dream_summary=%s WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
						dbcursor.execute(updateDreamSummary,(newDreamSummary,dreamYear,dreamMonth,dreamDay,userName))
						updatedDream=dbcursor.fetchall()
						dbConnection.commit()

					elif updateDreamOption=="6":
						clearConsole()
						pass
					print("The dream has been updated properly")
				pressToContinue()
				clearConsole()
				return updatedDream

			def showLastDream():
				clearConsole()
				if language=="1":
					lastDream="SELECT * FROM dream WHERE dream_user_name=%s ORDER BY dream_year DESC, dream_month DESC, dream_day DESC LIMIT 1"
					dbcursor.execute(lastDream,(userName,))
					showLastDreamDetails=dbcursor.fetchall()

					for row in showLastDreamDetails:
						print('Fecha: ' + str(row[3]) + '-' + str(row[2]) + '-' + str(row[1]))
						print('Titulo: ' + row[4])
						print('Resumen del sueño: ' + row[5])

				elif language=="2":
					lastDream="SELECT * FROM dream WHERE dream_user_name=%s ORDER BY dream_year DESC, dream_month DESC, dream_day DESC LIMIT 1"
					dbcursor.execute(lastDream,(userName,))
					showLastDreamDetails=dbcursor.fetchall()

					for row in showLastDreamDetails:
						print('Date: ' + str(row[2]) + '-' + str(row[3]) + '-' + str(row[1]))
						print('Title: ' + row[4])
						print('Dream summary: ' + row[5])
					
				pressToContinue()
				clearConsole()
				return showLastDreamDetails

			def showDream():
				clearConsole()
				if language=="1":
					dreamYear=input("Introduce el año del sueño: ")
					dreamMonth=input("Introduce el mes del sueño: ")
					dreamDay=input("Introduce el día del sueño: ")
					selectedDream="SELECT * FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
					dbcursor.execute(selectedDream,(dreamYear,dreamMonth,dreamDay,userName))
					showSelectedDream=dbcursor.fetchall()
					clearConsole()
					for row in showSelectedDream:
						print('Fecha: ' + str(row[3]) + '-' + str(row[2]) + '-' + str(row[1]))
						print('Titulo: ' + row[4])
						print('Resumen del sueño: ' + row[5])

				elif language=="2":
					dreamYear=input("Dream year: ")
					dreamMonth=input("Dream month: ")
					dreamDay=input("Dream day: ")
					selectedDream="SELECT * FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
					dbcursor.execute(selectedDream,(dreamYear,dreamMonth,dreamDay,userName))
					showSelectedDream=dbcursor.fetchall()
					clearConsole()
					for row in showSelectedDream:
						print('Date: ' + str(row[2]) + '-' + str(row[3]) + '-' + str(row[1]))
						print('Title: ' + row[4])
						print('Dream summary: ' + row[5])
					
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
					deleteDreamQuery="DELETE FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
					checkOption=checkDelete()
					if checkOption==1:
						dbcursor.execute(deleteDreamQuery,(deleteYear,deleteMonth,deleteDay,userName))
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
					deleteDreamQuery="DELETE FROM dream WHERE dream_year=%s AND dream_month=%s AND dream_day=%s AND dream_user_name=%s"
					checkOption=checkDelete()
					if checkOption==1:
						dbcursor.execute(deleteDreamQuery,(deleteYear,deleteMonth,deleteDay,userName))
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
			7) Registrar usuario (test)

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
			7) Register user (test)

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
				if option==7:
					clearConsole()
					insertUserAdmin()

