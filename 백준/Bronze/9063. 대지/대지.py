n = int(input())
x = set()
y = set()
if n == 1:
    print("0")
else:
    for i in range(n):
        a,b = map(int,input().split())
        x.add(a)
        y.add(b)
    hor = max(y) - min(y)
    ver = max(x) - min(x)
    print(hor * ver)