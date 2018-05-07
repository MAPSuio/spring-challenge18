from sys import stdin

shelf_width = 79
cur_width_used = 0
num_shelves = 1

for book_thickness in map(int, stdin):
    if cur_width_used + book_thickness > shelf_width:
        num_shelves += 1
        cur_width_used = book_thickness
    else:
        cur_width_used += book_thickness

print(num_shelves)
