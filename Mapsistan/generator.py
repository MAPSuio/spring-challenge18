import random

n = 1000000
m = 2500000

paths = set()

print(n, m)
for _ in range(m):
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)

    while (i == j) or frozenset([i,j]) in paths:
        j = random.randint(0, n - 1)

    paths.add(frozenset([i,j]))
    print(i, j)
