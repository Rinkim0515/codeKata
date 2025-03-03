def solution(my_string, n):
    answer = ''
    x = len(my_string) - n
    for idx,val in enumerate(my_string):
        if x <= idx:
            answer += val
        
    

    return answer