def solution(s):
    answer = 0
    for i in s:
        if i == "(":
            answer += 1
        else:
            answer -= 1
        if answer < 0:
            return False
            
            
        
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python',answer)

    return answer == 0