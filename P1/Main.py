from interfas_usuario import *
from interfas_mensajes import *
from interfaz_Admin import *
from imprimir import *
Usuario="Ninguno"
try:
	f=open("mensajes","r")
	f.close()
except FileNotFoundError:
	InitMensajes()
	"""Si no se encuentra el repositorio de mensajes, lo inicializa"""
	print("Creado un repositorio de mensajes\n")
"""Inicializa la variable señalando que el usuario no ha iniciado sesión"""
print("Ingrese Ayuda para ver los comandos")		
while True:
	"""Pide y realiza instrucciones de acuerdo al estado del usuario"""
	if Usuario=="Admin":
		print("Administrador detectado\n")
	Buffer=input("Ingrese una instrucción\n")

	if Buffer.lower()=="ayuda":
		ayuda(Usuario)
		"""Retorna los comandos disponibles según el estado de inicio de sesión"""

	elif Buffer.lower()=='salir':
		break
		"""Finaliza el programa"""

	elif Buffer.lower()=="iniciar sesion":				
		if Usuario!="Ninguno":
			print("Usted ya ha iniciado sesión")
		else:
			a=input("Ingrese su nombre de usuario\n")
			b=input("Ingrese su contraseña\n")
			Usuario=Inicio(a,b)
		"""Verifica las credenciales ingresadas con las credenciales de usuarios existentes"""

	elif Buffer.lower()=="crear usuario":				
		if Usuario=="Ninguno":
			Usuario=CrearUsuario(Usuario)
			"""Crea un nuevo Usuario e inicia sesión con sus credenciales"""
		elif Usuario =='Admin':
			Usuario=CrearUsuario(Usuario)
			Usuario="Admin"
			"""Crea un nuevo Usuario, pero sigue iniciado como Admin"""
		else:
			print("No puede registrar un nuevo usuario teniendo su sesión iniciada")

	elif Buffer.lower()=="eliminar usuario":
		if Usuario=='Admin':
			a=input("Ingrese el usuario a eliminar\n")
			while a.lower()=='admin':
				a=input("Inaceptable\nIngrese el Usuario a eliminar\n")
			EliminarUsuario(a)
		else:
			print("Usted no puede hacer esto\n")
			"""Si el Admin ha ingresado, elimina un usuario existente"""

	elif Buffer.lower()=="cerrar sesion":
		Usuario=CerrarSesion(Usuario)
		"""Define el usuario actual como desconectado"""

	elif Buffer.lower()=="revisar mensajes":
		if Usuario=="Ninguno":
			print("Necesita iniciar sesión para esto\n")
		else:
			ListaMensajes(Usuario)
			"""Retorna los mensajes relacionados con el usuario activo"""

	elif Buffer.lower()=='mensajes admin':
		if Usuario=='Admin':
			ListaAdmin()
		else:
			print("Usted no puede hacer esto\n")
		"""Lee todos los mensajes de todos los usuarios"""

	elif Buffer.lower()=="enviar mensaje":
		if Usuario=="Ninguno":
			print("Necesita iniciar sesión para esto\n")
		else:
			b=InterpretadorUsuarios(input("¿A quién desea enviar el mensaje?\n"))
			a=input("Ingrese el mensaje\n")
			EnviarMensaje(Usuario,a,b)
		"""Escribe un mensaje a otro/otros usuario existente"""

	elif Buffer.lower()=="archivar mensaje":
		if Usuario=="Ninguno":
			print("Necesita iniciar sesión para esto\n")
		else:
			lista=[]
			lista=str(input("Qué id desea eliminar?\n"))
			ArchivarMensajes(Usuario,InterpretadorParametroNumerico(Usuario,lista))
			"""Asigna el estado 'Archivado' a un mensaje del Usuario"""
	elif Buffer.lower()=="archivar admin":
		if Usuario=="Admin":
			parametro=input("ingrese las ids de los mensajes a archivar\n")
			ArchivarAdmin(parametro)
		else:
			print("usted no tiene los permisos nesesarios\n")
			"""Archiva mensajes con permisos de administrador"""

	elif Buffer.lower()=="imprimir mensajes":
		if Usuario=="Ninguno":
			print("Usted no puede hacer esto\n")
		else:
			Imprimir(Usuario)
			"""Imprime los mensajes del usuario, en un archivo aparte"""

	else:
		print("Input incorrecto, intente de nuevo\n")
		"""Vuelve a iniciar el ciclo de programa"""
