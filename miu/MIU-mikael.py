found = {
	0: [("MI",0)],
	"MI": 0,
}

lines = []

with open("mius.txt") as file:
	lines = file.read().splitlines()

def add(s,n):
	if s in found:
		return
	found[s] = n
	found[0].append((s,n))

def find(goal):
	while not goal in found:
		current = found[0]
		found[0] = []
		
		for word,n in current:
			if word.endswith("I"):
				add(word+"U",n+1)
			add(word+word[1:],n+1)
			for j in range(len(word)):
				if word[j:].startswith("UU"):
					add(word[:j]+word[j+2:],n+1)
				if word[j:].startswith("III"):
					add(word[:j]+"U"+word[j+3:],n+1)
		
		
	return found[goal]

sum = 0

for i in lines:
	sum += find(i)
	
print(sum)