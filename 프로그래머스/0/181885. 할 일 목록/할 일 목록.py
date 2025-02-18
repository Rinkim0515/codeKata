def solution(todo_list, finished):
    answer = []
    for idx, value in enumerate(todo_list):
        if finished[idx] != True:
            answer.append(value)
    return answer