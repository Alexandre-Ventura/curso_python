# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
# mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser
# aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual
# de cada um dos concorrentes e informar o vencedor da enquete.

respostas = []

while True:
    resposta = int(input("Qual o melhor Sistema Operacional para uso em servidores? \n"))
    if resposta != 1 and resposta != 2 and resposta != 3 and resposta != 4 and resposta != 5 and resposta != 6:
        break
    else: 
        respostas.append(resposta)

contador_1 = ((respostas.count(1)) / len(respostas))* 100
contador_2 = ((respostas.count(2)) / len(respostas))* 100
contador_3 = ((respostas.count(3)) / len(respostas))* 100
contador_4 = ((respostas.count(4)) / len(respostas))* 100
contador_5 = ((respostas.count(5)) / len(respostas))* 100
contador_6 = ((respostas.count(6)) / len(respostas))* 100

maior = contador_1

if (contador_2 > maior):
    maior = contador_2
if (contador_3 > maior):
    maior = contador_3
if (contador_4 > maior):
    maior = contador_4
if (contador_5 > maior):
    maior = contador_5
if (contador_6 > maior):
    maior = contador_6

print("Sistema Operacional              Votos      %  ")
print("-------------------              -----      -- ")
print(f"Windows Server:                    {respostas.count(1)}        {contador_1:.2f}")
print(f"Unix:                              {respostas.count(2)}        {contador_2:.2f}")
print(f"Linux:                             {respostas.count(3)}        {contador_3:.2f}")
print(f"Netware:                           {respostas.count(4)}        {contador_4:.2f}")
print(f"Mac OS:                            {respostas.count(5)}        {contador_5:.2f}")
print(f"Outro:                             {respostas.count(6)}        {contador_6:.2f}")
print("-------------------              -----")
print(f"Total:                             {len(respostas)} \n")

print(f"O Sistema Operacional mais votado foi o '', com {maior}")