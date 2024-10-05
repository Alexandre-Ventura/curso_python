# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.

listaA = []
listaB = []
listaC = []

for i in range(0,10):
    numero = int(input("Digite um número: "))
    listaA.append(numero)
    listaC.append(numero)
    numero2 = int(input("Digite outro número: "))
    listaB.append(numero2)
    listaC.append(numero2)
    
print(f"Primeira Lista: {listaA}")
print(f"Segunda Lista: {listaB}")
print(f"Terceira Lista: {listaC}")
