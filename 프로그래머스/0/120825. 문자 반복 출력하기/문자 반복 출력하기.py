def solution(my_string, n):
    answer = ''
    for i in my_string:
        x = i * n
        answer += x
    return answer