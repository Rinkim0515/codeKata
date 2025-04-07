def solution(i, j, k):
    answer = 0
    for idx in range(i,j +1):
        for idx2 in str(idx):
            if str(k) in idx2:
                answer += 1
        
        
    return answer