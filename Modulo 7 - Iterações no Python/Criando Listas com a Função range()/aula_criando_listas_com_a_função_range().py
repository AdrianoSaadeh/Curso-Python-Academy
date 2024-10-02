"""Aula - Criando Listas com a Função Range()
A função range significa intervalo e a ideia é range(inicio,fim,passos)
"""

# define apenas a parada (11 exclusive)
print(list(range(11)))

# inicia no 1 e vai ate 21 exclusive
print(list(range(1, 21)))

# inicia no 0 e vai ate 41 exclusive de 2 em 2
print(list(range(0, 41, 2)))

# Usando a função de intervalo para criar uma lista com todos os números pares de 0 a 30 incluídos
print(list(range(0, 31, 2)))
