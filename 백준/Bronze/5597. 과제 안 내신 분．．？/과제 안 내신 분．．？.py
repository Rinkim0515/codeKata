import sys

arr = [i for i in range(1,31)]
inputs = list(map(int,sys.stdin.read().split()))
for a in inputs:
    arr.remove(a)
arr.sort()
print(*arr)
    