def solution(a, b):
    case1 = (a ** 2) + (b ** 2)
    case2 = 2 * (a + b)
    case3 = a - b if a - b > 0 else -( a - b) 
    
    if a % 2 != 0 and b % 2 != 0:
        return case1
    elif a % 2 != 0 or b % 2 != 0:
        return case2
    else:
        return case3
    
    
   