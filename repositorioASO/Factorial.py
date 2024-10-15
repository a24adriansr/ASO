#!/bin/python3

#Programa que calcule o factorial

def factorial(numero):
    resultado = 1
    #No range se poñemos range(1, bla bla ) vai empezar en 1 e non en 0
    for i in range(1,int(numero)+1):
        resultado *= i
    return resultado

numero = input("Dame número: ")
r = factorial(numero)
print ("El factorial de {} es {}".format(numero,r))