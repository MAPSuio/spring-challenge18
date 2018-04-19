counter = 0
list_of_circles = []
with open("input.txt") as infile:
    for line in infile:
        x, y, r  = [int(w) for w in line.split()]
        list_of_circles.append((x, y, r))
for i in xrange(1000):
    for j in xrange(i+1, 1000):
        x1, y1, r1 = list_of_circles[i]
        x2, y2, r2 = list_of_circles[j]
        if (x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2:
            counter += 1

print counter
