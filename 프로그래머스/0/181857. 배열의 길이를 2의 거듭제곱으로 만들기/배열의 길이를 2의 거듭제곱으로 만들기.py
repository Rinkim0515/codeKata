def solution(arr):
    
    zero_count = 1
    if len(arr) & (len(arr) - 1) == 0:
        return arr
    while zero_count < len(arr):
        zero_count *= 2
    
    return arr + [0] * (zero_count - len(arr))