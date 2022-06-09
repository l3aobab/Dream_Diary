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

#Crear un usuario para esto
dbConnection=mysql.connector.connect(host="localhost",user=name,passwd=pswd)
dbcursor=ddbb.cursor()

#testear
def createUser():
	clearConsole()
	if language==1:
		userPassword=None
		userPasswordAuthentication=None
		print()
		print("""
-----------------------------

	Crea un usuario para poder continuar:

-----------------------------
		""")
		userName=print("Nombre del usurio: ")
		userPassword=getpass.getpass("Introduce una contraseña: ")
		userPasswordAuthentication=getpass.getpass("Confirma tu contraseña: ")
		if userPassword!=userPasswordAuthentication:
			print("Las contraseñas no coinciden, inténtalo de nuevo.")
			userPassword=getpass.getpass("Introduce una contraseña: ")
			userPasswordAuthentication=getpass.getpass("Confirma tu contraseña: ")			
		return userName,userPassword
	elif language==2:
		userPassword=None
		userPasswordAuthentication=None
		print()
		print("""
-----------------------------

	To continue, create and user:

-----------------------------
		""")
		userName=print("Username: ")
		userPassword=getpass.getpass("Enter a password: ")
		userPasswordAuthentication=getpass.getpass("Confirm your password: ")
		if userPassword!=userPasswordAuthentication:
			print("Passwords do not match, please try again")
			userPassword=getpass.getpass("Enter a password: ")
			userPasswordAuthentication=getpass.getpass("Confirm your password: ")			
		return userName,userPassword
