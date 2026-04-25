arr = [1,2,2,1,1,3,3]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
value = freq.values()

setV = set(value)
print(len(value))
print(len(setV))
return tr