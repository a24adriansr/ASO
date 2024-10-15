#!/usr/bin/python3
'''
#Métodos: fan accións sobre obxetos. Por exemplo,
#pon en maiúsculas os caracteres que introduza.
#Dille ao coche que acelere, dille que pare...
texto = "Este é un texto calquera"
'''


'''
print(texto.upper())
print(texto.lower())
#Neste caso len non é un método, é unha función, porque non 
#lle fai nada ao introducido, senón que nos da información
print(len(texto))
'''



#BUCLE FOR

listaIPs = ['192.168.10.1','192.168.10.12','192.168.10.13']


#Para cada Servidor na lista
for ips in listaIPs:
    comando = "Actualizando a IP{}".format(ips)
    print(comando)