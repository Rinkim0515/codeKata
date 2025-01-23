def solution(slice, n):
    answer = 1
    if slice > n:
        return answer
    else:
        while slice * answer < n:
            slice * answer
            answer += 1
        return answer
        
    