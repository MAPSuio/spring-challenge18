lines = []

with open("histogram.txt") as file:
	lines = file.read().splitlines()
	
sum = 0
for i in lines:
	since_last = -1
	skip = True
	for j in i:
		skip = not skip
		if skip:
			continue
			
		if j=='#':
			if since_last>=0:
				sum += since_last
			since_last = 0
		else:
			if since_last>=0:
				since_last += 1
	

print(sum)