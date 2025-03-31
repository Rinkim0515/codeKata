def solution(array):
    count_dict = {}
    
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    max_count = max(count_dict.values())
    
    mode_values = [key for key, value in count_dict.items() if value == max_count]
    
    if len(mode_values) == 1:
        return mode_values[0]
    else:
        return -1