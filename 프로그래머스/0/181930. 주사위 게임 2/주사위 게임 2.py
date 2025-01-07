def solution(a, b, c):
    count = 0
    num1 = a + b + c 
    num2 = (a * a) + (b * b) + (c * c)
    num3 = (a * a * a) + (b * b * b) + (c * c * c)
    cases = [ a == b, a == c, b == c]
    
    for i in cases :
        if i == 1:
            count += 1
        
    
    if count == 0 :
        return num1
    elif count == 1:
        return num1 * num2
    else :
        return num1 * num2 * num3
    
    
