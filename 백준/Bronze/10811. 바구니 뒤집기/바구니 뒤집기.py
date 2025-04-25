length, count = map(int,input().split())
arr = list(range(1,length+1))
for _ in range(count):
    a,b = map(int,input().split())
    arr[a - 1: b] = arr[a - 1 : b][::-1]
print(*arr)