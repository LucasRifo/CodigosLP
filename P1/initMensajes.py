import json
def InitMensajes():
    f=open("mensajes","w")
    lista=[]
    diccionario={}
    usuarios={}
    estado=["activo"]
    usuarios["emisor"]="Admin"
    usuarios["receptor"]=["Admin"]
    diccionario["mensaje"]="tema 0"
    diccionario["usuarios"]=usuarios
    diccionario["estado"]=estado
    lista.append(diccionario)
    f.write(json.dumps(lista))
    f.close()
    """Inicializa el repositorio de mensajes"""

