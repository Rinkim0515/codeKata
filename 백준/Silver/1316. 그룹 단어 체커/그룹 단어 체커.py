n = int(input())
words = [input() for _ in range(n)]
count = 0

    
for i in words:
    prev = ""
    visited = set()
    isGroup = True
    for ch in i:
        if ch != prev:
            if ch in visited:
                isGroup = False
                break
            visited.add(ch)
        prev = ch
    if isGroup:
        count += 1
print(count)
                
    



