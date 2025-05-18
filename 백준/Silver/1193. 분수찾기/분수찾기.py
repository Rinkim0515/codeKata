X = int(input())

line = 0
end = 0

while end < X:
    line += 1
    end += line

pos = X - (end - line)


if line % 2 == 0:
    a = pos
    b = line - pos + 1
    print(f"{a}/{b}")
else:
    a = line - pos + 1
    b = pos
    print(f"{a}/{b}")


