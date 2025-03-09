def solution(my_string):
    answer = ''
    alpha = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in alpha:
            answer += i
    return answer