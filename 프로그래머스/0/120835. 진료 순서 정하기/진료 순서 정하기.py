def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse = True)
    for i in emergency:
        rank = temp.index(i) + 1
        answer.append(rank)
    return answer