"""Aula - Métodos Nativos do Python
Uma Lista é um tipo de sequencia de Dados como: números inteiros,frações ou texto
"""

convidados = ["joão", "leila", "greg", "catia"]

print(convidados)
print(convidados[2])
print(convidados[-2])
# quando eu quiser pegar de trás pra frente eu não começo com '0' e sim com '-1'..-2...-3 e por ai vai

convidados[1] = "marcia"
print(convidados)

del convidados[-2]
# fiz isso para deletar um dos participantes sem mexer na minha lista

print(convidados)

print("\nAula começa aqui")
convidados.append("carlos")
print(convidados)

convidados.extend(["marcelo", "Diana"])
print(convidados)

print(("O primeiro participante é"), convidados[0])

print(len("mosca"))

print(len(convidados))
