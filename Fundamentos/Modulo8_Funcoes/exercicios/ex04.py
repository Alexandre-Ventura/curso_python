# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve
# converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
# conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a
# função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita
# que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converteHora(valorHora, valorMinuto):
    if (valorHora > 23) or (valorHora < 0) or (valorMinuto > 59) or (valorMinuto < 0):
        return None
    
    if (valorHora < 12):
        if (valorHora == 0):
            valorHora = 12
        return f"{valorHora:02d}:{valorMinuto:02d} AM"
        
    if (valorHora > 12):
        valorHora -= 12
        return f"{valorHora:02d}:{valorMinuto:02d} PM"
        
continuar = "S"
while (continuar == "S"):
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite o minuto: "))
    
    print(converteHora(hora, minuto))
    
    continuar = input("Deseja continuar: (S/N) ")