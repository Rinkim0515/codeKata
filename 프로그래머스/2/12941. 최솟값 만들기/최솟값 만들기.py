def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    answer = sum ( a * b for a, b in zip(A,B))

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer