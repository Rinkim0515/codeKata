def solution(s):
    answer = True
    p = 0
    y = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in s.lower():
        if i == "p":
            p += 1
        elif i == "y":
            y += 1
    if p != y:
        return False
    
    return True