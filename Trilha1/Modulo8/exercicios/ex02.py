#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
#argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verifica_numero(n):
    if(n > 0):
        return 'P'
    else:
        return 'N'
    
numero = int(input("entre com um numero: "))
verifica = verifica_numero(numero)
print(verifica)
    