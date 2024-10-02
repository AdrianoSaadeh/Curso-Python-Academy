"""Aula - Instruções Condicionais,Funções e Loops.ipynb
Objetivo: contar o numero de itens de uma lista cujo valor é menor que 20
se x<20 total aumentará em 1
se X>20 total não aumentará
"""


def conta(numeros):
    total = 0
    for x in numeros:
        if x < 20:
            total += 1
    return total


lista = [1, 3, 7, 8, 19, 54, 86, 12]
print(conta(lista))


# Usando o while precisou ordenar para a correta iteração do while
def count(numeros):
    print(numeros)
    numeros = sorted(numeros)
    print(numeros)
    total = 0

    while numeros[total] < 40:
        total += 1
    return total


numeros = [31, 51, 70, 100, 1, 35, 12, 24]
print(count(numeros))
