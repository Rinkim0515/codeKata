def solution(my_string, is_prefix):
    answer = 1
    if len(is_prefix) > len(my_string):
        return 0
    for i in range(0, len(is_prefix) - 1, 1):
        if my_string[i] == is_prefix[i]:
            continue
        else:
            return 0
    
    return answer