def comida_favorita(**kwargs):
    for chave in kwargs:
        print(f"{chave} gosta de {kwargs[chave]}")
        
comida_favorita(julia="Strogonoff", alexandre="Pizza", paulo="Arroz e Feijão")