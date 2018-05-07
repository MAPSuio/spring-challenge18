from random import shuffle

n = 1000000
word = list("kulturuke")

print("kulturuke")
for _ in range(n - 1):
    shuffle(word)
    print("".join(word))
