a = int(input())
b = int(input())
arr = []
for i in range(a, b+1):
    j = 2
    while j <= i:
        if i % j == 0:
            break
        j += 1
    if j == i:
        arr.append(i)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print("-1")

    
        