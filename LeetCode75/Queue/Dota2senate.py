from collections import deque

s = 'RDD'
R = deque()
D = deque()
n = len(s)
for i in range(n):
    if s[i] == 'R':
        R.append(i)
    elif s[i] == 'D':
        D.append(i)


while R and D:
    ri = R.popleft()
    di = D.popleft()
    if ri<di:
        R.append(ri + n)
    else:
        D.append(di + n)

if not D:
    print("Radiant")
        
elif not R:
    print("Dire")
        
    
