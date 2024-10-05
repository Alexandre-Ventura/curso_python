# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
# a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = {}

for mes in meses:
    temperaturas[mes] = float(input(f"Insira a temperatura média do mês de {mes}: "))
    
somaTemperatura = 0.0
for temperatura in temperaturas.values():
    somaTemperatura += temperatura
    
media_anual = (somaTemperatura / 12)

print(f"Media anual das temperaturas: {media_anual:.2f}")

for mes in meses:
    if (temperaturas[mes] >= media_anual):
        print(f"{mes} - {temperaturas[mes]:.2f}")
        