def solution(s):
    answer = ""
    for idx,val in enumerate(s):
        if idx == 0 or s[idx - 1] == " ":
            answer += val.upper()
        else:
            answer += val.lower()
    return answer