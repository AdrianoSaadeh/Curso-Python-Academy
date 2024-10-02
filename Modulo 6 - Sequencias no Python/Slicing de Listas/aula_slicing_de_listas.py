"""Aula - Slicing de Listas.ipynb
Slicing é fatiamento, no nosso caso fatiamento da nossa lista!
"""

participantes = ["joão", "leonardo", "marcos", "amanda"]
participantes
# pega do segundo elemento até o terceiro, pois o "3" indica que não está incluso
print(participantes[1:3])

# pega toda a lista até segundo elemento, exluindo o que vier a partir do índice 2 que é a terceira posição
print(participantes[:2])

# pegatudo a partir do segundo elemento da lista, representado pelo indice "1"
print(participantes[1:])

# mesmo resultado mas de trás para frente
print(participantes[-3:])

# pega o indice do elemento
print(participantes.index("amanda"))

novos = ["philip", "bruno"]
print(novos)

lista_top = [participantes, novos]
print(lista_top)

# ordena a lista
novos.sort()
print(novos)

participantes.sort()
print(participantes)

print(lista_top)
lista_top.sort(reverse=True)
print(lista_top)

numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros.sort(reverse=True)
print(numeros)
