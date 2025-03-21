def solution(s):
    answer = 0
    arr = s.split(" ")
    
    for idx,val in enumerate(arr):
        try:
            num = int(val)
            answer += num
        except ValueError:
            if val == "Z":
                answer -= int(arr[idx - 1])

    return answer