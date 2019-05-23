from gestor_mensajes import BuscarMensajes
def InterpretadorParametroNumerico(usuario,parametro):
    #parametro
    if parametro.isalnum():
        return [parametro]
    elif parametro == "*":
        lista=dict(BuscarMensajes(usuario))
        return list(lista.keys())
        """Señala a archivar todos los mensajes"""
    elif "," in parametro:
        return list(set(parametro.replace(","," ").split()))
        """Selecciona a archivar los números ingresados"""
    elif "-" in parametro:
        auxiliar=parametro.replace("-"," ").split()
        return list(range(int(auxiliar[0]),int(auxiliar[1])+1))
        """Señala a archivar todos los números en el rango ingresado"""
    else:
        NuevaLista=[]
        ListaVacía=[]
        for i in parametro:
            try:
                NuevaLista.append(int(parametro.pop()))
            except ValueError:
                continue
        if NuevaLista==ListaVacía:
            print("No se han ingresado id\n")
            pass
        else:
            return NuevaLista
            """Retorna una lista con sólo números"""
def InterpretadorUsuarios(parametro):
    return list(parametro.replace(","," ").split())
    """Entrega una lista de usuarios a partir del input de usuarios recibidos"""

