# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima
# a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(0,5):
    idade = int(input("Insira sua idade:"))
    idades.append(idade)
    
for i in range(0,5):
    altura = float(input("Insira sua altura: "))
    alturas.append(altura)
        
print(idades[::-1])
print(alturas[::-1])