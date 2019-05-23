import time
import sys
from gestor_mensajes import*
#from ..librerias_externas.winshell import *
def FechaHora():
    s=""
    s=s+time.strftime("%d/%m/%y")+"\n"
    s=s+time.strftime("%H:%M:%S")+"\n"
    return s
"""entrega la fecha y hora del equipo"""
def verSistema():
    systema=(sys.platform).strip("1234567890")
    return systema
"""entrega la plataforma en la que corre el programa"""
def buscadorEscritorio(Usuario):#recibe verSistema
    systema=verSistema()
    if systema=="win":
        import os
        import subprocess
        from win32com.shell import shell, shellcon
        a=(shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0))
        b=os.path.join(a,Usuario)
    elif systema=="linux":
        import subprocess
        import os
        a=subprocess.check_output(['xdg-user-dir', 'DESKTOP'])
        #print(a.decode("utf-8"))
        a=a.decode("utf-8")
        b=list(a)
        b.pop(-1)
        path=""
        for caracter in b:
            path=path+caracter
        b=os.path.join(path,Usuario)
        #print(path)
        return b
    else:
        print("no soportado")
        return "mac"
"""entrega la direcion absoluta del escritorio unida con el nombre del usuario"""
def Imprimir(Usuario):
    direccion=buscadorEscritorio(Usuario)
    if direccion == "mac":
        pass
    else:
        f=open(direccion,"w")
        f.write(FechaHora())
        mensajes=""
        lista=dict(BuscarMensajes(Usuario))
        for mensaje in lista:
            lista.get(mensaje).pop("estado")
            mensajes=mensajes+"    Mensaje N°: "+str(mensaje)+"\n"
            mensajes=mensajes+"        Emisor: "+str(lista.get(mensaje).get("usuarios").get("emisor"))+"\n"
            mensajes=mensajes+"            "+lista.get(mensaje).get("mensaje")+"\n"
            mensajes=mensajes+"        enviado a:"+"    "
            for r in (lista.get(mensaje).get("usuarios").get("receptor")):
                mensajes=mensajes+r+","
            mensajes=mensajes+"\n\n\n"
        f.write(mensajes)
        f.close()
        pass
        """Imprime los mensajes del usuario, en un archivo aparte"""
    
    
