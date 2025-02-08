def solution(numLog):
    answer = ''
    for index in range(len(numLog) -1):
        temp = numLog[index + 1] - numLog[index]
        if temp == 1:
            answer += 'w'
        elif temp == -1:
            answer += 's'
        elif temp == 10:
            answer += 'd'
        else:
            answer += 'a'
        
        
        
    return answer