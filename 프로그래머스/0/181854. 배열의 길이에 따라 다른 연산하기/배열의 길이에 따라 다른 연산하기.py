def solution(arr, n):
    answer = []
    if len(arr) % 2 != 0:
        for index,val in enumerate(arr):
            answer.append(val + n) if index % 2 == 0 else answer.append(val)
    else:            
        for index,val in enumerate(arr):
            answer.append(val + n) if index % 2 != 0 else answer.append(val)
            
                
        
            
    
    return answer