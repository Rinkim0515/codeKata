def solution(s):
    
    temp = []
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            temp.append(s[i])
        
        
    return "".join(sorted(temp))