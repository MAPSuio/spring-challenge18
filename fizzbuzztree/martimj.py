n = int(input())

children = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    children[u].append(v)

fizzes = buzzes = 0

def dfs(u, level):
    global fizzes, buzzes

    if level % 3 == 0:
        fizzes += 1
    if level % 5 == 0:
        buzzes += 1

    for v in children[u]:
        dfs(v, level + 1)

dfs(0, 1)
print(fizzes, buzzes)
