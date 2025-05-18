N = int(input())

count = 1
range_max = 1
while N > range_max:
    range_max += count * 6
    count += 1
print(count)