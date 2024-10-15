#!/usr/bin/python3

#Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido “pepe” y “abc123..” se indica “Has entrado al sistema”, 
# si no es así se da un error de usuario y/o contraseña no válidos.
from os import system
from getpass import getpass
from hashlib import sha512
#Borramos pantalla
system("clear")
'''
#Este é o meu programa

#Pedimos credenciais
usuario = input("Introduce o usuario:")
contrasinal = input("Introduce o contrasinal")

if usuario == "pepe" and contrasinal == "abc123..":
    print("Podes entrar no sistema")
else:
    print("Non podes")
    
'''

'''
Aquí está a clave sin cifrar
#Código de vieites, importamos getpass para que non se vexa o 
#contrasinal que introducimos por pantalla
usuarioPepe = "pepe"
password = "abc123.."

u = input("User:")
p = getpass("Contrasinal: ")

#Comprobamos 
if u == usuarioPepe and p == password:
    print("Podes entrar ao sistema")
else:
    print("Usuario e/ou contrasinal non válidos")
'''
#Preprograma
#Con getpass o usuario introduce texto sin que saia por pantalla
#Co método encode() pásase o string a UTF por defecto
#Con sha512 ese password en texto plano UTF pasámolo a un hash512
#Co método hexdigest() do hash xerado pasámolo a un formato hexadecimal seguro
#Utilizado para gardar en arquivo, bases de daos ou enviar por mail...
usuarioPepe = "pepe"
passwordSinCifrar = getpass("{} introduce o contrasinal: "\
    .format(usuarioPepe))
passwordCifrado = sha512(passwordSinCifrar.encode()).hexdigest()
print(passwordCifrado)


#Programa
print("Inicio de sesión")
u = input("Nombre:")
p = sha512(getpass("Contraseña: ").encode()).hexdigest()

if u == usuarioPepe and p == passwordCifrado:
    print("Podes entrar ao sistema")
else:
    print("Usuario e/ou contrasinal non válidos")