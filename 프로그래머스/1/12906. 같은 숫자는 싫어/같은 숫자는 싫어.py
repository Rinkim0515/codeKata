def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in range(len(arr)):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        else:
            answer.append(arr[i])
        
    return answer