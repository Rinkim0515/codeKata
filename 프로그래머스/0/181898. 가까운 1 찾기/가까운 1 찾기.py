def solution(arr, idx):
    answer = -1
    for i,val in enumerate(arr):
        if i >= idx:
            if val == 1:
                return i
                
    return answer