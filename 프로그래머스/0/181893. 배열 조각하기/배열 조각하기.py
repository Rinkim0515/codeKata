def solution(arr, query):
    answer = arr
    for idx,val in enumerate(query):
        if idx % 2 == 0:
            answer = answer[:val +1 ]
        elif idx % 2 != 0:
            answer = answer[val:]
    return answer