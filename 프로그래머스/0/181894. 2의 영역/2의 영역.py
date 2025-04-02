def solution(arr):
    answer = []
    if 2 not in arr:
        return [-1]
        
    indices = [i for i,x in enumerate(arr) if x == 2]
    
            
    return arr[indices[0]:indices[-1] + 1] if len(indices) != 1 else [2]