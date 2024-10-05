# função com parametro padrão;
def potencia(numero, expoente=2):
    """ Função que calcula a potência de um número.

    Args:
        numero (float): Número a ser calculado.
        expoente (int): Expoente a ser utilizado no calculo. Defaults to 2.

    Returns:
        float: Resultado do calculo da potencia
    """
    resultado = pow(numero, expoente)
    return resultado

#.....

n = float(input("Digite um número: "))
e = int(input("Expoente: "))

# nomeando os parametros 
print(f"Valor com o expoente: {potencia(expoente=e, numero=n)}")
print(f"Valor sem o expoente: {potencia(n)}")

