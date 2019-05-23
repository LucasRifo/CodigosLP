from gestor_mensajes import *
def ListaMensajes(usuario):
    lista=dict(BuscarMensajes(usuario))
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
    """Imprime mensajes activos del Usuario"""
def ayuda(A):
    if A=="Ninguno":
        print("Comandos:\n Iniciar Sesion\n Crear Usuario\n")
    else:
        print("Comandos:\n Enviar mensaje\n Revisar mensajes")
        print(" Archivar mensaje\n Imprimir mensajes\n Cerrar sesion")
        if A=="Admin":
            print(" Mensajes Admin\n Archivar Admin")
    print(" Ayuda\n Salir\n")
    pass
    """Imprime comandos disponibles"""

def CerrarSesion(A):
    if A=="Ninguno":
        print("Usted no está ingresado")
    else:
        print("Cerrando sesión")
        A="Ninguno"
    return A
    """Cierra la sesión iniciada"""
