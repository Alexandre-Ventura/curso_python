# Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 

notas = []
cont = 1

while (cont < 5):
    nota = float(input("Insira a nota: "))
    notas.append(nota)
    cont = cont + 1
    
nota_geral = sum(notas)
media = round(nota_geral / 4)

print(notas)
print(media)