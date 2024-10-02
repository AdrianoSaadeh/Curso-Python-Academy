"""Aula - Iteração com Dicionários
Queremos saber quanto Carlos gastou no supermercado, e pra isso teremos que multiplicar os preços pelas quantidades
"""

preços = {"macarrão": 4, "lasanha": 5, "hamburguer": 2}
quantidades = {"macarrão": 6, "lasanha": 10, "hamburguer": 10}

gasto = 0
for x in preços:
    print(x)
    gasto += preços[x] * quantidades[x]
    print(gasto)

print("Gastos com produtos de 5 dolares ou mais")

preços = {"macarrão": 4, "peixe": 5, "hamburger": 2}
quantidades = {"macarrão": 6, "peixe": 10, "hamburger": 0}

dinheiro_gasto = 0
for i in quantidades:
    if preços[i] >= 5:
        dinheiro_gasto += preços[i] * quantidades[i]
    else:
        dinheiro_gasto = dinheiro_gasto

print(dinheiro_gasto)


print("Gastos com produtos de menos de 5 dolares")

preços = {"macarrão": 4, "peixe": 5, "hamburger": 2}
quantidades = {"macarrão": 6, "peixe": 10, "hamburger": 0}

dinheiro_gasto = 0
for i in quantidades:
    if preços[i] < 5:
        dinheiro_gasto += preços[i] * quantidades[i]
    else:
        dinheiro_gasto = dinheiro_gasto

print(dinheiro_gasto)
