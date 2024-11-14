# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def mostraDigito(num):
    a = str(num)
    if len(a) > 1:
        if a[0] == "0":
            return len(a) - 1
        else:
            return len(a)
    return len(a)
    
n = int(input("Entre com um número: "))
print(f"O nuḿero {n} tem {mostraDigito(n)} digitos")