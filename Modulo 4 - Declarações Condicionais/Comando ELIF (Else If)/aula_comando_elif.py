"""Aula - Comando ELIF. O computador sempre lê seus comandos de cima para baixo! (ELIF é uma abreviação de Else If)"""

def compare_com_oito(y):
    if y > 8:
        return 'Maior'
    elif y < 8:
        return 'Menor'
    elif y < 0:
        return 'Negativo'
    else:
        return 'Igual'

print(compare_com_oito(9))
print(compare_com_oito(2))
print(compare_com_oito(-12))
# deveria dar 'negativo' mas como o computador lê de cima para baixo a primeira opção que atendia era 'Menor'

def compare_com_oito(y):
    if y > 8:
        return 'Maior'
    elif y < 0:
        return 'Negativo'
    elif y < 8:
        return 'Menor'
    else:
        return 'Igual'

print(compare_com_oito(-12))
# nessa resposta como troquei a ordem de 'negativo' e 'Menor' e -12 atendia os dois, ele me deu o primeiro resultado!

