"""Aula - Trabalhando com Matriz"""

import numpy as np

x = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(x)
print(type(x))
print(x.shape)

x[1, 3] = 18
print(x)

print(x[1, 2])

y = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [100, 99, 98, 97], [21, 31, 57, 9]])
print(y)
print(y.shape)