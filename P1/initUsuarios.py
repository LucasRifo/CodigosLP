import json
def InitUsuarios():
    f=open("usuarios","w")
    lista=[]
    dicc={}
    dicc["usuario"]="Admin"
    dicc["clave"]="all_your_messages_are_belong_to_us"
    lista.append(dicc)
    f.write(json.dumps(lista))
    f.close()
    """Inicializa el repositorio de Usuarios"""