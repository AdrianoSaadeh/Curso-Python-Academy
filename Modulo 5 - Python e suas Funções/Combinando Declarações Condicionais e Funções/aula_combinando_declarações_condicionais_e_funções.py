"""Aula - Combinando Declarações Condicionais e Funções

Se Carlos poupou pelo menos  100 reais até o final de semana ele ganha + 15 reais de sua mãe
Mas
Se ele não conseguir poupar pelo menos R$ 100 até o final de semana ele não ganha nada
"""


def adicione_15(m):
    if m >= 100:
        m = m + 15
        return print(m)
    else:
        return print(f"Guarda mais carlos! Você tem apenas {m}")


adicione_15(230)

adicione_15(99)
