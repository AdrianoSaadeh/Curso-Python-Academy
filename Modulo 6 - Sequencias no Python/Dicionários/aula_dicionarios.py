dicionario = {"k1": "prato", "k2": "garfo", "k3": "faca", "k4": "colher"}
print(dicionario)

print(dicionario["k1"])

dicionario["k5"] = "copo"
print(dicionario)

dicionario["k2"] = "panela"
print(dicionario)

dep_trabalhadores = {"dep_1": "carlos", "dep_2": ["marcela", "joao", "thaina"]}
print(dep_trabalhadores)
print(dep_trabalhadores["dep_2"])

time = {}
time["goleiro"] = "claudio"
time["zagueiro"] = "bebeto"
time["atacante"] = "neymar"
time["ponta esquerda"] = "pato"
time["ponta direita"] = "robinho"

print(time)
print(time["zagueiro"])
print(time.get("atacante"))
