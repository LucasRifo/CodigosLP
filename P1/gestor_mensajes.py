from herramientas_json import *
def BuscarMensajes (usuario):
    copia=LectorMensajes()
    personal=[]
    for elemento in copia:
        if  ((usuario == elemento.get("usuarios").get("emisor") or
            usuario in elemento.get("usuarios").get("receptor"))
            and not ( "archivado" in elemento.get("estado") or
            usuario in elemento.get("estado"))):
            personal.append(elemento)
    return enumerate(personal)
    """Retorna los mensajes relacionados con el Usuario"""

def EnviarMensaje(emisor,mensaje,receptores):
    listaReceptores=[]
    if type(listaReceptores)!=type(receptores):
        listaReceptores.append(receptores)
    else:
        listaReceptores=receptores
    for receptor in listaReceptores:
        if not ExisteUsuario(receptor):
            print("el Usuario "+ listaReceptores.pop
            (listaReceptores.index(receptor))+" no existe")
    if len(listaReceptores)>0:
        copia=LectorMensajes()
        NuevoMensaje={}
        Usuarios={}
        Usuarios["emisor"]=emisor
        Usuarios["receptor"]=listaReceptores
        NuevoMensaje["mensaje"]=mensaje
        NuevoMensaje["usuarios"]=Usuarios
        NuevoMensaje["estado"]=["activo"]
        CrearMensaje(NuevoMensaje)
        print("mensaje enviado")
        pass
        """Envía el mensaje a los receptores"""
    else:
        print("no hay receptores para el mensaje ")
        pass
    """Envia un mensaje a los receptores que existan"""
def ArchivarMensajes(usuario, listaIds):
    listaLocal=[]
    listaGlobal=[]
    for Id in listaIds:
        listaLocal.append(BuscarIdLocal(usuario,Id))
    for mensaje in listaLocal:
        listaGlobal.append(BuscarIdGlobal(mensaje))
    MensajesGlobal=LectorMensajes()
    try:
        for Id in listaGlobal:#clasificacion del tipo de archivado
            if MensajesGlobal[Id].get("usuarios").get("emisor") == usuario:
                MensajesGlobal[Id].get("estado")[0]="archivado"
            else:
                MensajesGlobal[Id].get("estado").append(usuario)
        ActualizarMensajes(MensajesGlobal)
        pass
    except TypeError:
        print("Uno o más mensajes detectados fuera del índice\n")
    """Archiva los mensajes señalados"""
    """Si se detecta alguna ID fuera del índice de mensajes,"""
    """la función no archiva ningún mensaje"""
def BuscarIdGlobal(mensaje):
    indice=dict(BuscarMensajesGlobal())
    for ind in list(indice.keys()):
        if indice.get(ind)==mensaje:
            return ind
    """Entrega la Id global del mensaje entregado""" 
def BuscarMensajesGlobal():
    copia=LectorMensajes()
    return enumerate(copia)
    """Entrega una lista enumerada de todos los mensajes""" 
def BuscarIdLocal(usuario,Id):
    IndicePersona=dict(BuscarMensajes(usuario))
    if IndicePersona.get(int(Id)) != None:
        return IndicePersona.get(int(Id))
    else:
        print ("no existe un mensaje con ese Id\n")
        pass
    """Entrega el mensaje con la Id local del usuario entregado"""
def AArchivar(ids):
    MensajesGlobal=LectorMensajes()
    try:
        for Id in ids:#clasificacion del tipo de archivado
            MensajesGlobal[int(Id)].get("estado")[0]="archivado"
        ActualizarMensajes(MensajesGlobal)
        pass
    except IndexError:
        print("Uno o más mensajes detectados fuera del índice\n")
        """Archivar mensajes como admin"""
        """Si se detecta alguna ID fuera del índice de mensajes,"""
        """la función no archiva ningún mensaje"""
