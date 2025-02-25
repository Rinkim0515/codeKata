def solution(my_string, m, c):
    answer = ''
    for i in range(0, len(my_string), m):
        
        temp = my_string[i: i + m]
        answer += temp[c - 1]
    return answer