

def is_composite(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count >= 3

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if is_composite(i):
            answer += 1
    return answer