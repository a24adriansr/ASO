#!/usr/bin/python3

#Crea una aplicación que permita adivinar un número generado aleatoriamente entre el 1 y el 100.
# El programa va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. 
#Nos devolverá el número de intentos, luego podemos modificarlo poniendo un número máximo de intentos
#antes de que termine el juego.
#El programa termina cuando se acierta el número.
#Nos pregunta si queremos jugar otra partida
#Que borre toda a pantalla cando se execute o script 

#Para eliminar elementos duplicados dunha lista
'''A = [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, ]
B = set(A)
print(A)
print(B)'''

#Con esto "paramos a execución entre número e número nun bucle"
#sig = input()


from random import randint
from os import system

'''
#Generar número aleatorio

#Borramos a pantalla
system('clear')
print("-"*45) #Imprimimos 45 guións así
#Xeramos un novo número entre 1 e 100
nOculto = randint(1,100)
print(nOculto)


nIntentos = 0


while True:
    nAposta =  int(input("Introduce un número enteiro entre 1 e 100: "))
    nIntentos = nIntentos + 1
    if nOculto > nAposta:
        print("O número oculto é maior")
    elif nOculto < nAposta:
        print("O número oculto é menor")
    else:
        print("Achertaches!!")
        print("Acertaches en {} intentos".format(nIntentos))
        break
    '''


################PROGRAMAMOS QUE SE POIDA VOLVER A XOGAR#######################

jugar = True

while True:
#Generar número aleatorio

    #Borramos a pantalla
    system('clear')
    print("-"*45) #Imprimimos 45 guións así
    #Xeramos un novo número entre 1 e 100
    nOculto = randint(1,100)
    print(nOculto)


    nIntentos = 0


    while jugar:
        nAposta =  int(input("Introduce un número enteiro entre 1 e 100: "))
        nIntentos = nIntentos + 1
        if nOculto > nAposta:
            print("O número oculto é maior")
        elif nOculto < nAposta:
            print("O número oculto é menor")
        else:
            print("Achertaches!!")
            print("Acertaches en {} intentos".format(nIntentos))
            break

#Preguntamos se quere xogar outra vez
    pedirSi = input('Queres xogar outra vez? (s/n)').lower()
    try:
        if pedirSi == 's':
            jugar = True
       
        else:
            print("Abur!")
            break
    
    except:
        print("Aprende a escribir")

        #FALTA REMATAR BEN O EJERCICIO CANDO PIDE S, N OU OUTRA COUSA