#Definimos función saúdo

def saludo():
    print("Hola")

#Función suma con dous valores
def sumar(n1,n2):
    rSuma = int(n1) + int(n2)
    return

#Función contas

def contas(n1,n2):
    rSuma = int(n1) + int(n2)
    rMulti = int(n1) * int(n2)
    rDiv = int(n1) / int(n2)

    r = {}
    r.setdefault("rSuma",rSuma)
    r.setdefault("rMulti",rMulti)
    r.setdefault("rDiv",rDiv)

    return r


def fibonacci(n):
    secuencia = [0, 1]  # Inicializamos con los primeros dos números

    for i in range(2, n):
        seguinte_num = secuencia[-1] + secuencia[-2]  # Suma de los dos últimos
        if seguinte_num > n:
            break  # Terminamos si el siguiente número excede el límite
        secuencia.append(seguinte_num)

    return secuencia

# Pedir el número máximo hasta donde se generará la sucesión
numero = int(input("introduce o número máximo da sucesión: "))

# Generar y mostrar la sucesión de Fibonacci
resultado = fibonacci(numero)
print(f"Sucesión de Fibonacci hasta {numero}: {resultado}")



    
def executarComando(comando):
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