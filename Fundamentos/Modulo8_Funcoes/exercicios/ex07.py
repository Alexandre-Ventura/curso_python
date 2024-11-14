# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reversoNumero(num):
    num_invertido = str(num)[::-1]
    return num_invertido

n = int(input("Digite um número: "))
print(f"{n} --> {reversoNumero(n)}")        