def fruta(n):
    lista = ['abacaxi', 'pera', 'maça', 'banana']
    if n>3:
        raise IndexError("O valor excede o número de elementos da lista")
    else:
        return lista[n]


print(fruta(5))