MOD = 100000007
n = int(input())
if n == 1:
	print(0)
elif n == 2:
	print(1)
else:
	prev2 = 0
	prev1 = 1
	for i in range(3, n+1):
		current = (i-1)*(prev1 + prev2) % MOD
		prev2 = prev1 
		prev1 = current
	print(prev1)