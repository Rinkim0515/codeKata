def solution(my_strings, parts):
    answer = ''
    count = 0
    for idx,(i,j) in enumerate(parts):
        string1 = my_strings[idx]
        answer += string1[i:j+1]
        
        
        
    return answer