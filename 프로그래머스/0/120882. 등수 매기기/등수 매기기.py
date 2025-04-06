def solution(score):
    avg = [sum(s)/2 for s in score]

    sorted_avg = sorted(enumerate(avg), key=lambda x: -x[1])

    rank = [0] * len(score)  
    current_rank = 1

    for i, (idx, val) in enumerate(sorted_avg):
        if i > 0 and val == sorted_avg[i - 1][1]:
            rank[idx] = rank[sorted_avg[i - 1][0]]
        else:
            rank[idx] = i + 1 

    return rank