def solution(s):
    last_seen = {}
    answer = []
    
    for idx, val in enumerate(s):
        if val in last_seen:
            answer.append(idx - last_seen[val])
        else:
            answer.append(-1)
        last_seen[val] = idx
            
        

        
    return answer