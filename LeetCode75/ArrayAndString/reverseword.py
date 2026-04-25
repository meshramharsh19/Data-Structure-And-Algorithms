n = input().split()
sent = list(n)
new_sent = []
for  i in range (len(sent)-1, -1,-1):
	new_sent.append(sent[i])
print(*new_sent)