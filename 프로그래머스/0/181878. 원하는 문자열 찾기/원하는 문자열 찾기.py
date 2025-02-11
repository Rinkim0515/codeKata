def solution(myString, pat):
    answer = 0
    if len(pat) > len(myString):
        return 0
    else:
        if pat.lower() in myString.lower():
            return 1
        else:
            return 0
        
    