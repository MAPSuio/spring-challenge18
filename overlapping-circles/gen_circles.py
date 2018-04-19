from random import randint

def generate_circles(filename):
    outfile = open(filename, "w")
    for i in xrange(1000):
        x = randint(-1000, 1000)
        y = randint(-1000, 1000)
        r = randint(1, 500)
        outfile.write('%d %d %d\n' % (x, y, r))
    outfile.close()

generate_circles("input.txt")
