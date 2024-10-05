# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O
# vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
# seguintes intervalos de valores:
# 1. $200 - $299
# 2. $300 - $399
# 3. $400 - $499
# 4. $500 - $599
# 5. $600 - $699
# 6. $700 - $799
# 7. $800 - $899
# 8. $900 - $999
# 9. $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

salarioBase = 200
vendedores = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
    valor_venda = float(input("Informe o valor das vendas do vendendor: "))
    salario = (valor_venda * 0.09) + salarioBase
    indice = int(salario / 100) - 1
    if (indice > 9):
        indice = 9
    elif (indice < 1):
        indice = 1
    print(indice)
    vendedores[indice - 1] += 1

for i in range(0, 9):
    print(f'{i * 100 + 200} - {(i + 1) * 100 + 199} - {vendedores[i]}')
    
    
        

        
