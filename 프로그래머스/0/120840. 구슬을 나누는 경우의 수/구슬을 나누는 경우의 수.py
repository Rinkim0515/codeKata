import math

def solution(balls, share):
    answer = math.factorial(balls) // (math.factorial(share) * math.factorial(balls - share))
    return answer