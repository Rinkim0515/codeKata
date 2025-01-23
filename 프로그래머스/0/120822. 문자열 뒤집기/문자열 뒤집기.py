def solution(my_string):
    answer = []
    for i in my_string:
        answer += i
    answer.reverse()
    
    return ''.join(answer)