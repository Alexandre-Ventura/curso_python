#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que
#é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
#função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    valorFinal = ((taxaImposto * custo) / 100) + custo
    return valorFinal

t = float(input("Entre com a taxa de imposto: "))
c = float(input("Entre com o valor do custo: "))
vF = somaImposto(t,c)
print(vF)