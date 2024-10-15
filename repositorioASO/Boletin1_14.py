#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia.
#No se puede utilizar el operador de potencia (**) o la función pow


#10 elevado a 5-, base ^ exponente
#10^5 = 10*10*10*10*10
base = int(input("Dame un número: "))
exponente = int(input("Dame outro: "))
potencia = 1

for n in range(exponente):
    potencia *= base
print("{}^{} = {}".format(base,exponente,potencia))