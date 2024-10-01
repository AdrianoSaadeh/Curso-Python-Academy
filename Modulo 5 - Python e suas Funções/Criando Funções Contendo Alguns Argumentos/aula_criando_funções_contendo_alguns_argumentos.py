"""Aula - Criando Funções Contendo Alguns Argumentos"""


def conta(a, b, c):
    resultado = a - b * c
    print("parametro a é igual", a)
    print("parametro b é igual", b)
    print("parametro c é igual", c)
    return print(resultado)


conta(10, 2, 6)
