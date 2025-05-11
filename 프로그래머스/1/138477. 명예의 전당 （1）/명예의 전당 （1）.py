def solution(k, score):
    answer1 = []
    answer2 = []
    for i in range(len(score)):
        if i < k :
            answer1.append(score[i])
            
        else:
            if score[i] > min(answer1):
                answer1.remove(min(answer1))
                answer1.append(score[i])
        answer2.append(min(answer1))
    return answer2