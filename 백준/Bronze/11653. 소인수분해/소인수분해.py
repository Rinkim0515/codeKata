num = int(input())

a = 2
while num > 1:
    if num % a == 0:
        print(a)
        num //= a
        
        
    else:
        a += 1
