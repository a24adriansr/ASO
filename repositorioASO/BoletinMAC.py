#!/usr/bin/python3

from subprocess import PIPE,Popen
from re import compile,findall

comando = 'ip a'
'''
ejecComando = Popen(comando, shell=True, stdout=PIPE)
salComando = ejecComando.stdout.read().decode('utf-8')
ejecComando.stdout.close()
print(salComando)

print("-"*20)


'''
def execComando(comando):
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