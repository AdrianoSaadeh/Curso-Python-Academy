# Defina uma função, chamada compare_as_duas(), com dois argumentos. Se o primeiro for maior que o segundo, deixe imprimir \"Maior\".
# Se o segundo for maior, deve imprimir \"Menos\". Deixe imprimir \"Igual\" se os dois valores forem o mesmo número."


def compare_as_duas(primeiro, segundo):
    if primeiro > segundo:
        print("Primeiro Maior")
    elif segundo > primeiro:
        print("Primeiro é menor")
    else:
        print("São iguais")


compare_as_duas(99, 47)
compare_as_duas(1, 5)
compare_as_duas(10, 10)
