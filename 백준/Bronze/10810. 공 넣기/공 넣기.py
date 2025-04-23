length, count = map(int,input().split())
arr1 = [0] * length
while count != 0:
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        arr1[idx] = k
    count -= 1
print( *arr1 )

    