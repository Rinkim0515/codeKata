def solution(a, d, included):
    
    answer = 0
    arr = []
    for index, val in enumerate(included):
        arr.append(a + d * index)
        if val:
            answer += arr[index]
            
    return answer