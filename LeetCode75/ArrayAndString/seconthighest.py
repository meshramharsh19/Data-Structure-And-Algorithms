n = int(input())
s = list(map(int, input().split()))

# ns = sorted(s)
# print(ns[n-2])

max = float('-inf')
index = 0
sec_max = float('-inf')

for i in range (len(s)):
    if max < s[i]:
        max = s[i]
        index = i
s.remove(s[index])

for i in range (len(s)):
    if sec_max < s[i]:
        sec_max = s[i]
print(sec_max)    