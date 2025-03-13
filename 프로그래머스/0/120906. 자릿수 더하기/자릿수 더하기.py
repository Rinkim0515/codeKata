def solution(n):
    answer = 0
    temp = n
    while temp > 0:
        answer += temp % 10
        temp = temp // 10
        
    return answer