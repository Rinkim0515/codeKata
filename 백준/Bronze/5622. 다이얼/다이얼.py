groups = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input()
total = 0
for ch in word:
    for i in range(len(groups)):
        if ch in groups[i]:
            total += i + 3
            break
print(total)                
