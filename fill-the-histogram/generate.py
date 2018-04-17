from random import randint

def histstr(vals):
    m = max(vals)
    bars = ['#' * v + ' ' * (m - v) for v in vals]
    transposed = [' '.join(list(b)) for b in zip(*bars)]
    return '\n'.join(transposed[::-1])

def generatetest(n):
    return [randint(1,n+1) for _ in range(n+1)]

def visualfill(hist):
    lines = hist.split('\n')
    filled = []
    for line in lines:
        walls = [i for i, b in enumerate(line) if b == '#']
        if len(walls) < 2:
            continue
        for w1, w2 in zip(walls, walls[1:]):
            water = '~ ' * ((w2 - w1 - 1)/2)
            line = line[:w1+2] + water + line[w2:]
        filled.append(line)
    return '\n'.join(filled)

def slowsolve(hist):
    filled = visualfill(hist)
    return filled.count('~')

if __name__ == "__main__":
    test = histstr(generatetest(2000))
    with open("histogram", "w") as f:
        f.write(test)
