# -*- coding: latin-1 -*-
import json
from initUsuarios import *
from initMensajes import *
def Inicio(Usuario,Clave):
    try:
        f=open("usuarios","r")
    except FileNotFoundError:
        InitUsuarios()
        f=open("usuarios","r")
    copia=json.loads(f.read())
    f.close()
    for elemento in copia:
        if Usuario==(elemento.get("Usuario"))and Clave==elemento.get("Clave"):
            print("Sesión iniciada con éxito\n")
            return Usuario
    print("Usuario no encontrado o contraseña inválida\n")
    return "Ninguno"
    """Comprueba las credenciales de seguridad para iniciar sesion en el JSON"""

def CrearUsuario(A):
    flag= False
    dicc={}
    try:
        f=open("usuarios","r")
    except FileNotFoundError:
        InitUsuarios()
        f=open("usuarios","r")
    copia=json.loads(f.read())
    f.close()
    a=input("Ingrese su nombre de Usuario\n")
    while flag==False:
        while a.replace(" ","")=="" or (a.lower()).strip()=="ninguno":
            a=input("Debe ingresar un nombre de Usuario\n")
        for i in range(len(copia)):
            if a.lower() == (copia[i]["Usuario"]).lower():
                a=input("Usuario ya existente\nIngrese otro nombre de Usuario\n")
                break
            elif i==len(copia)-1:
                flag=True
    dicc["Usuario"]=a
    b=input("Ingrese su contraseña\n")
    while b.replace(" ","")=="":
        b=input("Debe ingresar una contraseña\n")
    dicc["Clave"]=b
    b=input("Ingrese su nombre\n")
    while b.replace(" ","")=="":
        b=input("Debe ingresar su Nombre\n")
    dicc["Nombre"]=b
    b=input("Ingrese su Apellido\n")
    while b.replace(" ","")=="":
        b=input("Debe ingresar su Apellido\n")
    dicc["Apellido"]=b
    while flag==True:
        b=input("¿Desea agregar algo más? (S/N)\n")
        if b.lower()=="s":
            b=input("¿Qué desea agregar? (Ej: Apellido, edad)\n")
            if (b.lower()).capitalize() in dicc.keys():
                print("No puede sobreescribir sus datos\n")
            else:
                c=input("¿Qué valor desea agregarle a "+b+"?\n")
                dicc[b]=c
        elif b.lower()=="n":
            flag=False
        else:
            print("Input incorrecto\n")
    copia.append(dicc)
    f=open("usuarios","w")
    f.write(json.dumps(copia))
    f.close()
    print("Nuevo usuario añadido\n")
    return a
    """Crea un nuevo usuario, si es que éste no existe en el JSON"""
####
def LectorMensajes():
    try:
        f=open("mensajes","r")
    except FileNotFoundError:
        InitMensajes()
        f=open("mensajes","r")
    copia=json.loads(f.read())
    f.close()
    return copia
    """retorna una copia del JSON de mensajes"""
####
def CrearMensaje(nuevo):
    print("nuevo mensaje")
    copia=LectorMensajes()
    copia.append(nuevo)
    f=open("mensajes","w")
    f.write(json.dumps(copia,indent=4))
    f.close()
    pass
    """Escribe un nuevo mensaje en el JSON"""
####
def ActualizarMensajes(lista):
    f=open("mensajes","w")
    f.write(json.dumps(lista,indent=4))
    f.close()
    pass
    """Actualiza los mensajes a archivar"""
def ExisteUsuario(usuario):
    try:
        f=open("usuarios","r")
    except FileNotFoundError:
        InitUsuarios()
        f=open("usuarios","r")
    listaUsuarios=json.loads(f.read())
    for infoUsuarios in listaUsuarios:
        if usuario in infoUsuarios.get("Usuario"):
            return True
    return False
    """Comprueba la existencia del receptor"""
def ListaUsuarios():
    f=open("usuarios","r")
    listaUsuarios=json.loads(f.read())
    f.close()
    return listaUsuarios
    
