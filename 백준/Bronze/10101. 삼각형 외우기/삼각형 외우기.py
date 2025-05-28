angles = [int(input()) for _ in range(3)]
total = sum(angles)
unique = len(set(angles))

if total != 180:
    print("Error")
elif unique == 1:
    print("Equilateral")
elif unique == 2:
    print("Isosceles")
else:
    print("Scalene")