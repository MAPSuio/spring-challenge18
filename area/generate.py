import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.5 + 0.5*np.sin(20/(x-2))

def gen_random_points(N):
    return np.random.random(N)

np.random.seed(2)
N = 1000000
x = gen_random_points(N)
y = f(x)
print(sum(y)/x.shape[0])

with open('coordinates.txt', 'w') as f:
    for i, (x, y) in enumerate(zip(x, y)):
        f.write(f'{x} {y}')
        if i < N-1:
            f.write('\n')