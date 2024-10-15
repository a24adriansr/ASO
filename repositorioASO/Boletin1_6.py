#!/usr/bin/python3
#Algoritmo que pida números hasta que se introduzca un cero. 
#Debe imprimir la suma y la media de todos los números introducidos.
'''
listaNum = [1,2,4,78,98,34]

print(listaNum)
listaNum.remove(2) #Eliminamos polo valor da lista

print(listaNum)
listaNum.pop(0) #Eliminamos polo indíce da lista (o primeiro posto que é o 0)
print(listaNum)
listaNum.append(34343) #Engadimos o valor ao final da lista
print(listaNum)
listaOrdenada = sorted(listaNum)

print(listaNum)
print(listaNum[-1])
print(listaNum[2:4])
print(listaNum.sort())
print(listaOrdenada)
'''


#Creamos unha lista vacía
listaNumeros = []   #list()

#Co while True facemos un bucle infinito, xa que é un bucle que non sabemos canda acabará xa que depende do usuario (Neste caso non sabemos cando vai pulsar 0 o usuario)
while True:
    n = int(input("Dame un número: "))
    if n == 0:
        break
    else:
        listaNumeros.append(n)
        #Imos vendo a lista
        print(listaNumeros)
#Mostramos como queda a lista dos números
print(listaNumeros)

# A suma dos elementos dunha lista conseguímola con sum(listaNumeros)
suma = sum(listaNumeros)
nElementos = len(listaNumeros)
print("La suma de los números es " + str(suma))
print("A media dos números é "+ str(suma/nElementos))