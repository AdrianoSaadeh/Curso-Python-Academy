def salario(hrs_trab):
    return hrs_trab * 100


def com_bonus(hrs_trab):
    return salario(hrs_trab) + 200


print(salario(40))
print(com_bonus(40))
