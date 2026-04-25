# Q1: Move zeros to end
n = int(input("number of elements: "))
A = []
for i in range (0,n):
	a = int(input("enter number: "))
	A.append(a)

b = []
c = []
output = []

for i in range (n):
	if A[i] == 0:
		b.append(A[i])
	else:
		c.append(A[i])

		
output = c + b
print(*output)		
	
