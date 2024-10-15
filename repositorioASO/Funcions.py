#!/usr/bin/python3

from misfunciones import contas
#Definimos unha funcion
####################
def saludo():
    print("Hola")
####################

#Chamamos á función
saludo()

for i in range(10):
    saludo()

#######
#Un script

##Definimos funcion suma con dos parámetros
def sumar(num1funcion,num2funcion):
    rSuma = int(num1funcion) + int(num2funcion)
    return rSuma
###########################################
#num1 = input("Introduce un número 1: ")
#num2 = input("Introduce un número 2: ")
#print( " suma de {} + {} = {}".format(num1,num2,sumar(num1,num2)))


lista1 = [23,56,78,56,78]
lista2 = [1,2,3,4,5,6]

for i in range(len(lista1)):
    print(sumar(lista1[i],lista2[i]))


for i in range(len(lista1)):
    #print("{} + {} = {}".format())
    print(contas(lista1[i],lista2[i]))
    resultado = contas(lista1[i],lista2[i])
    print("{} + {} = {}".format(lista1[i],lista2[i],resultado['rSuma']))
    print("{} * {} = {}".format(lista1[i],lista2[i],resultado['rMulti']))
    print("{} / {} = {}".format(lista1[i],lista2[i],resultado['rDiv']))




#Funcion que calcule o factorial

def factorial(numero):
    resultado = 1
    #No range se poñemos range(1, bla bla ) vai empezar en 1 e non en 0
    for i in range(1,int(numero)+1):
        resultado *= i
    return resultado

#Función de saída
def execComando(comando):
    from subprocess import PIPE,Popen
    from re import compile,findall
    pComando = Popen(comando, shell=True, stdout=PIPE, stderr=PIPE)
    erro = pComando.stderr.read().decode('utf-8')
    sComando = pComando.stdout.read().decode('utf-8')
    pComando.stdout.close
    if not erro:
        return sComando
    else:
        return erro
    
#Ahora buscamos as MACS

comando1 = 'ip n'

patronMAC = "(?:[0-9a-f]{2}:){5}[0-9a-f]{2}"
listaMACs = compile(patronMAC).findall(execComando(comando1))
print(listaMACs)


def passValida(contrasinal):
    from re import compile,search

    contrasinal= str(input("Introduce un contrasinal: "))

    patronEspacios = compile('\s')

    valida = False

    if len(contrasinal) >= 8 and not compile('\s').search(contrasinal):
        print("Seguinte")
        contador = 0 #Contador de condicións
        if compile('[a-z]').search(contrasinal):contador+=1 #Se o contrasinal ten algunha minúscula
        if compile('[A-Z]').search(contrasinal):contador+=1 #Se o contrasinal ten algunha maiúscula
        if compile('[0-9]').search(contrasinal):contador+=1 #Se o contrasinal ten números
        if compile('\W').search(contrasinal):contador+=1 # Se hai simbolos
        if contador >= 3:valida=True

    else:
        print("Contrasinal non válido")
    return valida