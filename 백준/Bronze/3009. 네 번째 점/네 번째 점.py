x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in x:
    if x.count(i) == 1:
        x_ans = i
        break

for i in y:
    if y.count(i) == 1:
        y_ans = i
        break

print(x_ans, y_ans)