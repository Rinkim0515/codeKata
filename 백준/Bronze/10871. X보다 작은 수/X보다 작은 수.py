count, least = map(int,input().split())
arr1 = list(map(int,input().split()))
if count == len(arr1):
    arr2 = []
    for i in arr1:
        if i < least:
            arr2.append(i)
    print(*arr2)