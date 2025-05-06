def solution(n):
    num = 1234567
    f0, f1 = 0, 1
    for _ in range(n):
        f0, f1 = f1, f0 + f1
    return f0 % num
