def solution(num_list):
    answer = 0
    case1 = 1
    case2 = 0
    for i in num_list:
        case1 *= i
        case2 += i
    
    if case1 > case2 * case2:
        answer = 0
    else:
        answer = 1

    
    
    return answer