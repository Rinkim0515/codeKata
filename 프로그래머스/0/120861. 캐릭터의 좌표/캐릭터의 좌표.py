def solution(keyinput, board):
    answer = [0,0]
    max_x = (board[0] - 1) //2
    max_y = (board[1] - 1) //2
    
    for key in keyinput:
        if key == "up" and answer[1] < max_y:
            answer[1] += 1
        elif key == "down" and answer[1] > -max_y:
            answer[1] -= 1
        elif key == "left" and answer[0] > -max_x:
            answer[0] -= 1
        elif key == "right" and answer[0] < max_x:
            answer[0] += 1

    
    
    return answer