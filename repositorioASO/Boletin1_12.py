#Programa que calcula o factorial de un número que se pide

#5! = 5*4*3*2

#7! = 7*6*5*4*3*2

factorial = 1
print("Calculando factorial")
numero = int(input("Dame un número: "))

for n in range(1,numero+1):
    factorial = factorial * n
print("El factorial de {} es {}".format(numero,factorial))