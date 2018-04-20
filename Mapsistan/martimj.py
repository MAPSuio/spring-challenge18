n, m = map(int, input().split())
num_components = n

# if parent[i] < 0 then i is a root and -parent[i] is the tree's depth
# this is used to keep the tree's depth as short as possible
parent = [-1 for _ in range(n)]

def find(i):
    if parent[i] < 0:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]

def union(i, j):
    global num_components

    ii = find(i)
    jj = find(j)

    if ii == jj:
        return
    else:
        # two components are connected for the first time
        num_components -= 1

    isize = -parent[ii]
    jsize = -parent[jj]

    if isize < jsize:
        parent[ii] = jj
    elif isize > jsize:
        parent[jj] = ii
    else:
        parent[ii] = jj
        parent[jj] -= 1 # depth increased by 1

for _ in range(m):
    i, j = map(int, input().split())
    union(i, j)

print(num_components - 1)
