#prime number or not :

n = int(input("how many numbers to check : "))

for i in range(n):
	num = int(input("enter number to check : "))
	for j in range(2, num):
		if num % j == 0:
			print("NO")
			break;
	else:
		print("YES")