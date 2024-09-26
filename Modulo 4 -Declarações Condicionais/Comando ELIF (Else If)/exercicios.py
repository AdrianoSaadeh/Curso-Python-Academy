""" Atribua 200 a variavel x. Crie o seguinte trecho de código: Se x> 150, imprima \"Grande\"; 
    Se x> 100 e x <= 150, imprima \"Médio\"; e se x <= 100, imprima \"Pequeno\". 
    Use as palavras-chave if, elif e slse em seu código,

    "Altere o valor inicial de x para ver como sua saída irá variar."""

x = 150
if x > 150:
    print("Grande")
elif x > 100 and x <= 150:
    print("Médio")
else:
    print("Pequeno")

""" Mantenha as duas primeiras condições do código anterior. Adicione uma nova instrução ELIF, de modo que, eventualmente, o programa imprima 
\"Pequeno\" se x> = 0 e x <= 100, e \"Negativo\" se x <0. Deixe x levar o valor de 50 e depois de -50 para verifique se o seu código está correto."""

x = 100
if x > 150:
    print("Grande")
elif x > 100 and x <= 150:
    print("Médio")
elif x >= 0 and x <= 100:
    print("Pequeno")
else:
    print("Negativo")
