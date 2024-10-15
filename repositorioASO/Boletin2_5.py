#!/bin/python3

#Facer un diccionario do arquivo axenda.txt

pathArquivo = './agenda.txt'

#Abrimos arquivo
#Non sei que fai o escrito a continuación
#Abre o Arquivo como lectura, pero non sei que é as fr
with open(pathArquivo,'r') as fr:
    #Pasar o arquivo a unha lista de liñas
    listaLineas = fr.readlines()

print(listaLineas)    

#Temos axenda e sería interesante pasala a un diccionario, onde 
# a clave é o nome do contacto e o valor o teléfono

dictAgenda = {}
#Recorremos lista de contactos

for l in listaLineas:
    #print(l)
    ll = l.split(':') #"Lista da línea"
    #print(ll)
    if len(ll) == 2:
        contacto = l.split(':')[0].strip()
        telefono = l.split(':')[1].strip()
        # print(contacto)
        # print(telefono)
        # print('-'*20) #Delimitar bucles
        #Rellenamos o diccionario
        dictAgenda.setdefault(contacto,telefono)
        
print(dictAgenda)

u = input("Teléfono de: ")
if u in dictAgenda:
    print(dictAgenda[u])
else:
    print('Ese usuario no está en la agenda')