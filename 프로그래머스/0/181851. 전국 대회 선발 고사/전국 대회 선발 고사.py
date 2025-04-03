def solution(rank, attendance):
    answer = []
    for i in range(len(rank)):
        if attendance[i] :
            answer.append((rank[i],i))
    answer.sort()
    a = (answer[0][1]) * 10000
    b = (answer[1][1]) * 100
    c = answer[2][1]
        
    return a + b + c