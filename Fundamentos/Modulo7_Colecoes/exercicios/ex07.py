# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []

# Recebendo valores

for i in range(0,5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    soma = 0
    produto = 1 
    for num in numeros:
        soma = num + soma
    for num in numeros:
        produto = num * produto
        

print(numeros)
print(f"A soma de todos os números da lista é: {soma}")
print(f"A multiplicação entre todos os números da lista resulta em: {produto}")
