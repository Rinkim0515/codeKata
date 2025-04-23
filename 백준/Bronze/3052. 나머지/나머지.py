import sys
arr = map(int, sys.stdin.readlines())
s = set()
for i in arr:
    s.add( i % 42)
print(len(s))

