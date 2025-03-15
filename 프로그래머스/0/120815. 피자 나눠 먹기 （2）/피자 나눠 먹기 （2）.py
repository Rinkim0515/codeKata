def solution(n):
    a, b = n, 6
    while b:
        a, b = b, a % b 

    lcm = (n * 6) // a
    return lcm // 6