num = list(map(int, input().split()))
k = int(input())
l = len(num)
lt = (len(num)-k) + 1
ans = 0 
for i in range(lt):
        ca = sum(num[i:i+k]) / k
        if ca > ans:
            ans = ca
print(ans)