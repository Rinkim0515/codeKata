count = int(input())
arr1 = list(map(int,input().split()))
if count == len(arr1):
    arr2 = []
    arr2.append(min(arr1))
    arr2.append(max(arr1))
    print( *arr2 )