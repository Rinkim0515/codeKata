def solution(n):
    answer = 0
    for i in range(1, n + 1):
        temp = n - i * (i - 1) // 2
        if temp % i == 0:
            a = temp // i
            if a >= 1:  
                answer += 1
    return answer