W = list(map(int, input().split()))
Max_W = int(input())
W.sort()
L = len(W)

total = 0
people = 0

for i in W:
	if total + i <= Max_W:
		total += i
		people += 1
	else:
		break
print(people)
		
	
# def max_people(weights, W):
#     weights.sort()
    
#     total = 0
#     count = 0
    
#     for w in weights:
#         if total + w <= W:
#             total += w
#             count += 1
#         else:
#             break
            
#     return count


# # Example
# weights = [10,20,30,40, 50, 60, 70]
# W = 80
# print(max_people(weights, W))  # Output: 2