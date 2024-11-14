# Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos
# do vetor.

listaA = []
soma = 0 

for i in range(0,10):
    numero = int(input("Digite um número: "))
    listaA.append(numero)
    soma = (numero **2) + soma
       
print(listaA)
print(soma)