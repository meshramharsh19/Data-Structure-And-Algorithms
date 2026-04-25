s = input().strip()
l = len(s)

for i in range(l):
	count = 0
	for j in range(l):
		if s[i] == s[j]:
			count += 1	
	if count == 1:
		print(s[i])
		break;
else:
	print(-1)
	