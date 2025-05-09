def solution(food):
    answer = ''
    for idx, val in enumerate(food):
        if val >= 2:
            for i in range(val // 2):
                answer += f"{idx}"
    return answer + "0" + answer[::-1]
    

