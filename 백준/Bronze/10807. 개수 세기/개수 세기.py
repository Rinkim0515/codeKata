count = int(input())
arr = list(map(int,input().split()))
index = int(input())
if count == len(arr):
    count = 0
    for i in arr:
        if i == index:
            count += 1
    print(count)