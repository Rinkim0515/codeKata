def solution(number):
    answer = 0
    num = 0
    for i in str(number):
        num += int(i)
    
    answer = num % 9
    return answer