day = input().strip()
n = int(input())

days = {
'monday':1,
'tuesdyay':2,
'wednesday':3,
'thursday':4,
'friday':5,
'saturday': 6,
'sunday':7
}

start = days[day]
count = n // 7 
rem = n%7

for i in range(rem):
	if(start + i) % 7 == 6:
		 count += 1

print(count)

