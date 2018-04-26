# Generates a k-ary tree, where the probability of a node being included
# decreases for each level. Nodes are indentified by a number >= 0, and
# the output starts with the number of nodes on a single line, followed
# by all paths in the tree. The number of paths in a tree is always equal
# to the number of nodes minus one, so it is not given as input. The root
# node is at level 1, and is always identified by the number 0.

import random

k = 2 # max number of children per node
num_levels = 30

# Have to save paths before printing, because we need to print number of
# nodes first, which we don't know before having generated all the paths
paths = []

# Probability of child being generated
def p(level):
    return 1 - (level / num_levels)**2

def generate(node, level):
    global paths

    if (level < num_levels):
        for _ in range(k):
            if random.random() < p(level):
                child = len(paths) + 1

                paths.append((node, child))
                generate(child, level+1)

# Start from root 0 and level 1
generate(0, 1)

print(len(paths))
for path in paths:
    parent, child = path
    print(parent, child)
