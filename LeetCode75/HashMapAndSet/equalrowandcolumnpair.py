grid = [[3,2,1],[1,7,6],[2,7,7]]

row = {}
column = {}
count = 0
for i in range(len(grid)):
    row[i+1] = grid[i]
    
    col = []  # 🔥 new list for each column
    for j in range(len(grid)):
        col.append(grid[j][i])
    
    column[i+1] = col

print(row.values())
for r in row.values():
    for c in column.values():
        if r == c:
            count += 1

    
print(count)