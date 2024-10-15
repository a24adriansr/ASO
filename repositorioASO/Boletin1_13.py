#!/usr/bin/python3

#Escribir un programa que imprima todos os números pares entre dous números que se lle pidan ao usuario
print("Calculamos os pares entre dous números")

numero0 = int(input("Dame o primeiro numero."))
numero1 = int(input("Dame o segundo número:"))


for n in range(numero0,numero1+1):
    if n % 2 == 0:
        print(n)
    else:
        pass