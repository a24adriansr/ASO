from subprocess import PIPE,Popen
from re import compile,findall

def execComando(comando):
    ejecComando = Popen(comando, shell=True, stdout=PIPE, stderr=PIPE)
    erro = ejecComando.stderr.read().decode('utf-8')
    sComando = ejecComando.stdout.read().decode("utf-8")
    ejecComando.stdout.close()

    if not erro:
        return sComando
    else:
        return erro