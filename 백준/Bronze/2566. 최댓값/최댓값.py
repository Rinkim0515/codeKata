matrix = [ list(map(int,input().split())) for _ in range(9)]
max_val = 0
x,y = 0, 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_val:
            max_val = matrix[i][j]
            x, y = i, j
print(max_val)
print(x+1, y+1)
               
        