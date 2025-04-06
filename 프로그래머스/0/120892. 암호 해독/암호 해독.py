def solution(cipher, code):
    answer = ""
    for idx, val in enumerate(cipher):
        if (idx + 1) % code == 0:
            answer += val
    return answer