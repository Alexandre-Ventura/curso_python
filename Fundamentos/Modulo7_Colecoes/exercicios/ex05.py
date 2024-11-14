# Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. Armazene os números pares na lista PAR e
# os números IMPARES na lista impar. Imprima as três listas.

numeros = []
par = []
impar = []
cont = 1

while(cont < 21):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if (numero % 2) == 0:
        par.append(numero)
    else:
        impar.append(numero)
    cont = cont + 1
    
print(f"Lista inteira: {numeros}")
print(f"Lista Par: {par}")
print(f"Lista Impar: {impar}")
