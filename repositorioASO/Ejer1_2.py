#!/usr/bin/python3

'''
El área A de un triángulo se puede calcular a partir del valor de dos de sus lados, a y b, y del ángulo ø que estos forman 
entre sí con la fórmula: A = 1/2 * a * b * sin(ø). Diseña un programa que pida el valor de los dos lados (en metros),
el valor del ángulo que estos forman (en grados), y muestre el valor del área.
[Ten en cuenta que la función sin de Python trabaja en radianes, así que el ángulo que se lea en
grados hay que pasarlo a radianes sabiendo que π radianes son 180 grados].

'''
from os import system
from math import radians, sin

#O meu código
lado_1 = float(input("Indica o primeiro lado:"))
lado_2 = float(input("Indica o segundo lado:"))
valorAngulo = float(input("Indica o ángulo:"))
#Pasamos o ángulo a Radianes
anguloRadianes = radians(valorAngulo)
#Facemos o seno do ángulo para posteriormente facer o cálculo final
anguloSeno = sin(anguloRadianes)
areaDef = lado_1 * lado_2 * anguloSeno /2

print(areaDef)
#####################################################

#print("Cálculo del área de un triángulo")

#try:
#    anguloProba = int(input("Introduce ángulo: "))
#    salida = "O triángulo con ángulo {}".format(anguloProba)
#    print(salida)

#except:
#    print("Introduce un ángulo válido")

#Código de Manuel
#Borramos toda la pantalla
#Pedimos por pantalla
'''system("clear")
print("Cálculo del área de un triángulo")
ladoA = float(input("Lado A: "))
ladoB = float(input("Lado B: "))
anguloGrados = (float(input("Ángulo en grados:")))
#Pasamos a radianes
anguloRadianes= radians(anguloGrados)
#Realizamos o cálculo
area = ladoA * ladoB * sin(anguloRadianes) / 2
#Cortamos con .\ para que non quede moi largo o código a continuación:
salida = "O triángulo de lados {}cm, {}cm e ángulo {}Grados ten de área {}".\
      format(ladoA,ladoB,anguloGrados,area)
print(salida)'''