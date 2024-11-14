# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = []
vogais = []
cont = 1

while(cont < 11):
    caracter = input("Insira um caracter: ")
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        vogais.append(caracter)
    else:
        caracteres.append(caracter)
    cont = cont + 1
    
consoantes = len(caracteres)    
print(f"A quantidade de consoantes é {consoantes}")
print(caracteres)



    
