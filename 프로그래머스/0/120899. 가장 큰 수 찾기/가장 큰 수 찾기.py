def solution(array):
    answer = []
    
    for idx,val in enumerate(array):
        if max(array) == val:
            answer.append(val)
            answer.append(idx)
    return answer