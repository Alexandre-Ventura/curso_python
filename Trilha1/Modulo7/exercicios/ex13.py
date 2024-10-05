# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;

lista = []
maior_media = []
menor_sete = []

while True: 
    valores = int(input("Insira um número: "))
    if (valores == -1):
        break
    else:
        lista.append(valores)

# a. Mostre a quantidade de valores que foram lidos:
print(f"Quantidade de valores que foram lidos: {len(lista)}")
print("-" * 30)

# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(lista)
print("-" * 30)

# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
for valores in lista[::-1]:
    print(valores)  
    
print("-" * 30)

# d. Calcule e mostre a soma dos valores;
soma_valores = 0
for valores in lista:
    soma_valores += valores 

print(f"A soma de todos os elementos que tem na lista é: {soma_valores}")      
print("-" * 30)

# e. Calcule e mostre a média dos valores;
media_valores = (soma_valores / len(lista))

print(f"A média de todos os valores contidos na lista é: {media_valores}")
print("-" * 30)

# f. Calcule e mostre a quantidade de valores acima da média calculada;
for valores in lista:
    if valores > media_valores:
        maior_media.append(valores)
        
print(f"Esses são os elementos que possuem um valor maior que a media da lista: {maior_media}")
print("-" * 30)

# g. Calcule e mostre a quantidade de valores abaixo de sete;
for valores in lista:
    if valores < 7:
        menor_sete.append(valores)
    
print(f"Esses são os elementos que possuem um valor menor que sete: {menor_sete}")
print("-" * 30)


