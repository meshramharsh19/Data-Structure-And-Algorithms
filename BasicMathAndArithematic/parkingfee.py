h = int(input())

if h <= 2:
	fee = 100 * h
elif h > 2 and h <= 5:
	fee = (100 * 2) + ((h-2)*50)
elif h > 5:
	fee = (100 * 2) + (50*3) + ((h-5)*20)
print(fee)