def solution(num_list, n):
    case1 = []
    case2 = []
    for i in range(0,len(num_list),1):
        if i < n:
            case1.append(num_list[i])
        else:
            case2.append(num_list[i])
        
    return case2 + case1