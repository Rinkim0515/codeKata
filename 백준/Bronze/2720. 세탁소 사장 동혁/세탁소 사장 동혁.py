count = int(input())
for _ in range(count):
    i = int(input())
    arr = [] 
    while i > 0:
        arr.append(i // 25)
        i %= 25
        arr.append( i // 10)
        i %= 10
        arr.append( i // 5)
        i %= 5
        arr.append( i // 1)
        i %= 1
    print(*arr)    
        
    
    