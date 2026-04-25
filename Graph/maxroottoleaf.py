n, *rest = map(int, input().split())
values = rest[:n] 
edges_data = rest[n:-1]
k = rest[-1] 
adj = [[] for i in range(n+1)]
for i in range(0, len(edges_data), 2):
    u = edges_data[i]
    v = edges_data[i+1]
    adj[u].append(v)
    adj[v].append(u)

print(k)
print(edges_data)
print(values)
print(n)
print(*rest)
print(adj)