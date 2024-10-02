"""Aula - Tupla
# tupla é uma função automatica do python exemplo: x=(30,50,14) oq esta em parenteses é uma tupla
Tuplas não podem ser alteradas ou modificadas (não da pra acrescentar ou excluir elementos)
"""

x = (11, 12, 13)
print(x)

y = 44, 45, 46
print(y)

# não é uma tupla
a, b, c = 1, 4, 6
print(c)

print(x[0])

List = [x, y]
print(List)

nome, idade = "marcela,27".split(",")
print(nome)
print(idade)

nome = "adriano"
print(nome)


def info_retangulo(x, y):
    A = x * y
    P = 2 * (x + y)
    print("Area and Perimetro são de respectivamente: ", A, "e", P)


info_retangulo(3, 5)
