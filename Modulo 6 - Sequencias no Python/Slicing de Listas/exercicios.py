# Usando slicing de lista, obtenha os números 94 e 15
num = [8, 56, 87, 94, 15, 31]
print(num[3:5])

# Usando o slicing, extraia os primeiros quatro elementos da lista.
print(num[:4])

# Usando o slicing, extraia todos os elementos da lista a partir da 2ª posição.
print(num[1:])

# Usando o slicing, extraia os últimos 4 elementos da lista.
print(num[-4:])

# Qual é o índice do valor 15?
print(num.index(15))

# Crie uma lista chamada "dois_numeros". Sejam seus elementos os valores 1 e 2. Em seguida, crie um novo, denominado "todos_numeros",
# que conterá as listas "num" e "dois_numeros"
dois_numeros = [1, 2]
todos_numeros = [dois_numeros, num]
print(todos_numeros)

# Classifique todos os números na lista "num", do maior para o menor.
print(num)
num.sort(reverse=True)
print(num)
