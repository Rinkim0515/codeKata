def solution(arr):
    answer = 1
    length = range(len(arr))
    for i in length:
        for j in length:
            if arr[i][j] != arr[j][i]:
                return 0

    return answer