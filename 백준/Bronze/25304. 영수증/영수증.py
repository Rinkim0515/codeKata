total = int(input())
count = int(input())

for i in range(count):
    v,c = map(int,input().split())
    total -= v * c
if total == 0:
    print("Yes")
else:
    print("No")
  