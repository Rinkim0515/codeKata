def solution(n):
    answer = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            answer.append(i)
            n //= i
        i += 1
    if n > 1:
        answer.append(n)
    return sorted(list(set(answer)))