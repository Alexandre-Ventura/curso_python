# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no
# qual a soma das linhas, colunas e diagonais é a mesma. 

import numpy as np
import random 
    
def quadradoMagico():
    novo_array = np.empty(shape=(0,0))
    for i in range(0,9):
        num = random.randint(1,9)
        print(f"Número sorteado: {num}")
        novo_array = np.append(novo_array, num)
        print("Array : ", novo_array)
    return novo_array
    
print(quadradoMagico())
    
    
    