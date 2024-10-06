"""Aula - Números Aleatórios"""

import random

probabilidade = random.random()
print(probabilidade)

dado = random.randint(1, 6)
print(dado)

import numpy as np

print(np.random.randint(1, 10, (4, 6)))
