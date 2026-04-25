w = list(map(int, input().split()))
c = int(input())
w.sort()

curr_w = 0 
peop = 0 

for i in range(len(w)):
	if c > curr_w + w[i]:
		curr_w += w[i]
		peop += 1
print(peop)