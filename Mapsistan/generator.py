import random

n = 1000000
m = 2500000

print(n, m)
for _ in range(m):
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)

    while (i == j):
        j = random.randint(0, n - 1)

    # Fullt mulig at samme vei forekommer mer enn én gang
    print(i, j)
