def solution(a, b):
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    g = gcd(a, b)
    b //= g  
    
    
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    
    return 1 if b == 1 else 2