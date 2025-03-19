def solution(myString, pat):
    answer = ''
    temp = len(pat)
    for i in range(len(myString) + 1):
        if myString[i:temp + i] == pat:
            answer = myString[:temp + i]
    return answer