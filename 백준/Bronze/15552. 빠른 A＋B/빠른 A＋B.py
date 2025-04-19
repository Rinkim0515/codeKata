import sys
count = int(sys.stdin.readline())

for i in range(count):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    print(a + b)