from interfas_usuario import *
from interfas_mensajes import *
from gestor_mensajes import *
def ListaAdmin():
	lista = dict(enumerate(LectorMensajes()))
	mensajes=""
	for e in lista:
		lista.get(e).pop("estado")
		mensajes=mensajes+"    Mensaje N°: "+str(e)+"\n"
		mensajes=mensajes+"        Emisor: "+str(lista.get(e).get("usuarios").get("emisor"))+"\n" 
		mensajes=mensajes+"            "+lista.get(e).get("mensaje")+"\n"
		mensajes=mensajes+"        enviado a:"+"    "
		for r in (lista.get(e).get("usuarios").get("receptor")):
			mensajes=mensajes+r+","
		mensajes=mensajes+"\n\n\n"
	print(mensajes)
	pass
	"""Imprime todos los mensajes de todos los usuarios"""
def ArchivarAdmin(parametro):
    AArchivar(InterpretadorParametroNumerico("Admin",parametro))
    pass
    """Archivará un mensaje de cualquier usuario"""
def EliminarUsuario(Usuario):
	flag=False
	try:
		f=open("usuarios","r")
	except FileNotFoundError:
		InitUsuarios()
		f=open("usuarios","r")
		print("No hay usuarios que eliminar\n")
	copia=json.loads(f.read())
	f.close()
	for elemento in range(len(copia)):
		if Usuario==(copia[elemento].get("Usuario")):
			print("Usuario encontrado\n")
			del copia[elemento]
			print("Usuario eliminado\n")
			flag=True
			break
	if flag==False:
		print("No se ha podido encontrar al usuario en cuestión\n")
	else:
		f=open("usuarios","w")
		f.write(json.dumps(copia))
		f.close()
	pass
	"""Elimina un usuario ingresado pasado a la función"""
