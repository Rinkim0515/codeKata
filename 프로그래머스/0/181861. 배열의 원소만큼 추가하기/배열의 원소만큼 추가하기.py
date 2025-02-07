def solution(arr):
    answer = []
    for i in arr:
        for val in range(i):
            answer.append(i)
    return answer