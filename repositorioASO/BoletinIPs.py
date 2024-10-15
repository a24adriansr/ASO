#!/usr/bin/python3

#Imprimir lista de IPs do network interfaces


#Conseguir unha lista
from re import compile,findall
#Lemos o arquivo e pasámolo a unha lista de liás
pathInterfaces = '/etc/network/interfaces'
with open(pathInterfaces,'r') as fr:
    texto = fr.read()

print(texto)

#Buscamos IPs existentes e retornamos unha lista con elas

patronIP = "(?:[0-9]{1,3}\.{3}[0-9]{1,3})"
listaIP = compile (patronIP).findall(texto)
print(listaIP)