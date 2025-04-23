import sys
arr1 = list(map(int, sys.stdin.readlines()))
max_val = max(arr1)
print(max_val)
print(arr1.index(max_val) + 1)