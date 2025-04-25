count = int(input())
arr1 = list(map(int,input().split()))
N = max(arr1)
arr2 = [i / N * 100 for i in arr1]
print(sum(arr2) / count)
