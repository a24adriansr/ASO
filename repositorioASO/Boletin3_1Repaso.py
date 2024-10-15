#!/usr/bin/python3
"""
Programa que le o arquivo /etc/passwd dado un usuario que se pide por teclado, se existe,
devolve os siguientes datos: uid, gid, home, shell.. tamañoHome, grupo principal e grupoSecundarios
Se non existe devolve "Este usuario non existe no equipo"
"""
from os import system
from funcoes import execComando
#Pedimos usuario
usuario = input("Dime unha conta de usuario: ")

pathPasswd = '/etc/passwd'
#FR PORQUE É FILE READ
with open(pathPasswd,'r') as fr:
    lLineasPasswd = fr.readlines()

##Vamos a comprobar que la lista contiene el archivo
#print(lLineasPasswd)

#Xa temos a lista de liñas, recorremos unha a unha e dividimos cada línea nos seus campos
##root:x:0:0:root:/root:/bin/bash\n
##Recorrer toda a lista con un bucle

usuarioExiste = False
for linea in lLineasPasswd:
    #print(linea.strip()) #Aplicamos a cada línea o strip() para eliminar o '\n' e ver que funcionaría
    #Dividimos a línea nos campos que nos interesan
    lLinea = linea.strip().split(":")
    #print(lLinea)
    cuenta = lLinea[0]
    if usuario == cuenta:
        uid = lLinea[2]
        gid = lLinea[3]
        home = lLinea[5]
        shell = lLinea[6]
        #Calculamos o tamaño do home
        comando = 'du -sh {}'.format(home)
        tamHome = execComando(comando).split('/')[0].strip()
        print(tamHome)
        #Descubrimos grupos principal e secundario
        comando = 'groups {}'.format(cuenta)
        grupos = execComando(comando).split(':')[1].strip()
        gPrincipal = grupos.split(' ')[0].strip() #Obtenemos un string
        gSecundarios = grupos.split(' ')[1:]#Obtenemos unha lista


        #Comprobamos que o usuario ten ou non password
        pathShadow = '/etc/shadow'
        with open(pathShadow,'r') as fr:
            lShadow = fr.readlines()
        #Creamos un diccionario 'cuenta':'password'
        dShadow = {}
        for lineaShadow in lShadow:
            llineaShadow = lineaShadow.split(':')
            if len(llineaShadow[1]) > 50:
                tienePassword = True
            else:
                tienePassword = False
            dShadow.setdefault(llineaShadow[0],tienePassword)

        usuarioExiste = True
        break




#Ahora mostramos saída dependendo de se o usuario existe ou no
if usuarioExiste:
    print('conta: ',cuenta)
    print('uid:',  uid)
    print('gid: ', gid)
    print('grupos:', grupos)
    print('Grupo principal: ', gPrincipal)
    print('Grupos secundarios', ','.join(gSecundarios)) #Convertir a lista nun string de elementos separados por  ','
    print('home: ', home)
    print('Tamaño home: ',tamHome)
    print('shell: ',shell)
    print('Ten password: ',dShadow[cuenta])
    print('-'*20) #Separador de líneas
else:
    print("Ese usuario non existe")


#sudo cat /etc/shadow | grep root | cut -d : -f 2 | wc -c

