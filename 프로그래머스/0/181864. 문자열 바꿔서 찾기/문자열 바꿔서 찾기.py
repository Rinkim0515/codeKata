def solution(myString, pat):
    temp = ''
    for i in myString:
        if i == 'A':
            temp += 'B'
        else:
            temp += 'A'
    if pat in temp:
        return 1
    else:
        return 0
