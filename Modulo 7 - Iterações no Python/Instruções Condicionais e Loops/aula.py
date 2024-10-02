print(list(range(11)))

# 2^1, 2^2 ... 2^10
for n in list(range(11)):
    print(2**n, end=" ")

print()

# x%2 == 0 seria o mesmo que dizer se for um numero par
for x in list(range(21)):
    if x % 2 == 0:
        print(x)
    else:
        print(f"{x} é impar")
