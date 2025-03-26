def solution(arr, k):
    answer = []
    for i in range(0,len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
            
    if len(answer) < k:
        for i in range(len(answer),k):
            answer.append(-1)
    if len(answer) > k:
        while len(answer) != k:
            answer.pop()
    
    return answer