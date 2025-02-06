def solution(num_list):
    answer = num_list
    num1 = num_list[-2]
    num2 = num_list[-1]
    num3 = 0
    
    if num1 >= num2:
        num3 = num2 * 2
    else: 
        num3 = num2 - num1
    answer.append(num3)
    return answer