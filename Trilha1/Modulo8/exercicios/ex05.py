# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
# função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver
# atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valorPrestação, numDias):
    if (numDias == 0):
        valorFinal = valorPrestação
    else:
        valorFinal = valorPrestação + ((valorPrestação * 0.03) + (numDias * 0.001))
    return round(valorFinal, 2)

def mostraRelatorio():
    print("-"*50)
    print("--------------RELATÓRIO FINAL DO DIA--------------")
    print("-"*50)
    print("Quantidade de prestações pagas: ",len(valorTotal))
    print("Valor total das prestações pagas: R$",round(sum(valorTotal), 2))
    print("-"*50)

valorTotal = []

valor = 1 
while (valor != 0):
    valor = float(input("Digite o valor da prestação: "))
    if (valor == 0):
        break
    else:
        dias = int(input("Diga quantos dias a prestação está atrasada: "))
        print(valorPagamento(valor, dias))
        valorTotal.append(valorPagamento(valor, dias))        
            
mostraRelatorio()   