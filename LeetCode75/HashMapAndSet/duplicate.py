# arr = list(map(int, input().split()))
# l = len(arr)
# output = False
# for i in range(l):
#     for j in range(l):
#         if i == j :
#             pass
#         elif arr[i] == arr[j]:
#             # output = True
#             break
# print(output)



# hashmap
arr = list(map(int, input().split()))
hashmap = {}
output = False
for i in range(len(arr)):
    if arr[i] in hashmap:
        output = True
        break
    else:
        hashmap[arr[i]] = i
print(output)