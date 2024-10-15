#!/usr/bin/python3
from misfunciones import execcomando
#Pedimos usuario a buscar
u = input("Dime o teu usuario: ")

pathPasswd = '/etc/passwd'
with open(pathPasswd, 'r') as fr:
    lLineas = fr.readlines()
#print(lLineas)
#Definimos unha variable booleana que indicará se o usuario está ou non
uEsta = False
for l in lLineas:
    ll = l.strip().split(':')
    cuenta = ll[0]
    if cuenta == u:
        #print(ll)
        lDatosU = ll
        uEsta = True
        break


if uEsta:
    print(lDatosU)
    comandoTamHome = "du -sh {}".format(lDatosU)
    tamHome = execcomando(comandoTamHome).slit('/')
    print("Cuenta: ",lDatosU[0])
    print("UID: ",lDatosU[2])
    print("GID: ",lDatosU[3])
    print("Descripcion: ",lDatosU[4])
    print("Home: ",lDatosU[5])
    print("Tamaño do home", comandoTamHome)
    print("Shell: ",lDatosU[6])
else:
    print('Usuario no encontrado')

