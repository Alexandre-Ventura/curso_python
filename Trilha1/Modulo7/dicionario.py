# Fazer um programa que receba:
# Cadastro de uma qntd ilimitada de proprietários e seus respectivos apartamentos.
# Guarde essas informações em um dicionário, onde a chave de busca é o número do do apto.
# Para encerrar a digitação o número do apto deve ser -1.
# Em seguida, deve-se mostrar uma linguagem, em ordem crescente de apto: apto - nome do proprietário.
# No final apresente a quantidade total de aptos listados.

propietarios = {}

while True:
    apto = int(input("Digite o número do seu apto: "))
    if apto != -1:
        propietario = input("Propietário: ")
        propietarios.update({apto:propietario})
    else:
        break
    
edificio = dict(sorted(propietarios.items()))

for chave, valor in edificio.items():
    print(f"{chave} - {valor}")
    
print(f"Total de apartamentos: {len(edificio)}")