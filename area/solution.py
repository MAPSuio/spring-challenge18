with open('coordinates.txt', 'r') as f:
    lines = f.readlines()
s = sum(float(line.split()[1]) for line in lines)

N = 1000000
print(s/N)