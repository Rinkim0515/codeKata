def solution(num, k):
    answer = -1
    for idx,val in enumerate(str(num)):
        if val == str(k):
            answer = idx + 1
            break
            
    return answer