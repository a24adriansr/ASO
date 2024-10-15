#!/usr/bin/python3
#Escribir un programa que solicite un número de segundos y muestre por 
#pantalla dicha cantidad de tiempo en horas, minutos y segundos.



#segundos = int(input("Introduce os segundos"))
#minutos = segundos / 60
#horas = minutos / 60

#print(minutos)
#print (horas)
#print("Todo corresponde a {} horas {} minutos {} segundos ".format(horas,minutos,segundos))


'''Un modo de facelo sería sabendo que 1 hora = 3600 segundos
Si tiempoSegundos >= 3600 dividímolo entre 3600
3456789 / 3600 = x
Quedamos coa parte enteira, que son horas enteiras:
3456789 - 3600 * 960 = 789 segundos que aínda quedan por adxudicar
Xa sabemos que temos 960 horas, vamos a polos minutos
Se 789/60=13,15
Quédome coa parte enteira, que son os minutos enteiros:
789 - 60 * 13= 9 segundos
Así xa temos todo:
960horas - 13minutos - 9 segundos

'''

#Definimos variables
s = 0 #Segundos
m = 0 #Minutos
h = 0 #Horas

try:
    ##Leemos por teclado los segundos a convertir
    sTot = int(input("Introduce número de segundos: "))
    #Definimos unha variable de segundos temporales para ir facendo as contas e non perder o valor
    sTemp = sTot

    #Calculando o número de horas 
    if sTemp >= 3600:
        h = int(sTemp /3600)
        sTemp = sTemp - (3600 * h)
    if sTemp >= 60:
        m = int(sTemp/60)
        sTemp = sTemp - (60 * m)

    #Os segundos son os que quedan

    s = sTemp
    print(sTot)
    print(h)
    print(m)
    print(s)
    print("{} segundos son {} horas, {} minutos, {} segundos".format(sTot,h,m,s))
except:
    print("Introduce número de segundos válido")