# Jogo de Craps
# Se, na primeira jogada, você tirar 7 ou 11 = Vitoria
# 2,3 ou 12 na primeira jogada = Derrota
# 4,5,6,8,9 ou 10 na primeira jogada = Próprio ponto
# Objetivo é conseguir jogar novamente o seu ponto, caso tire 7 antes, perde o jogo.

import random

def craps_derrota_rodada1():
    print(f"Seu número é: {num}")
    print(f"Você teve azar, ao tirar esse número na primeira rodada você PERDEU!")
    
def craps_vitoria_rodada1():
    print(f"Seu número é: {num}")
    print(f"Você teve sorte, ao tirar esse número na primeira rodada você GANHOU!")
    
def craps_derrota():
    print(f"----------------DERROTA----------------")
    print(f"Você jogou 7 antes de jogar {pontuacao[0]}!")
    
def craps_vitoria():
    print(f"----------------VITÓRIA----------------")
    print(f"Você conseguiu! Jogou {pontuacao[0]}, antes de jogar 7!")
    
pontuacao = []
rodada = 1
continuar = "S"   

while (continuar == "S"):
    num = random.randint(2,12)
    print(f"Rodada: {rodada}")
    print(f"Esse é o número jogado: {num}") 
    
    if (rodada == 1) and (num  == 2) or (rodada == 1) and (num == 3) or (rodada == 1) and( num == 12):
        craps_derrota_rodada1()
        break
    
    elif (rodada == 1) and (num == 7) or (rodada == 1) and (num == 11):
        craps_vitoria_rodada1()
        break
    
    elif (rodada == 1) and (num in [4,5,6,8,9,10]):
        pontuacao.append(num)
        
    elif(rodada != 1) and (num == 7):
        craps_derrota()
        break
    
    elif (rodada != 1) and (num == pontuacao[0]):
        craps_vitoria()
        break
    
    print(f"Para ganhar você precisa rodar {pontuacao[0]} novamente, antes que tire 7!")
    continuar = input("Deseja continuar? (S/N) ")
    rodada += 1
        