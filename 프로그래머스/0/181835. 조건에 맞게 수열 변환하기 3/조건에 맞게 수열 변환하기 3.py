def solution(arr, k):
    iskOdd = [ x + k for x in arr]
    iskEven = [ x * k for x in arr]
    if k % 2 == 0:
        return iskOdd
        
    else:
        return iskEven
        