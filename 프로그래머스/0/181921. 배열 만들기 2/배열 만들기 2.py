def solution(l, r):
    answer = []
    numbers = ["5"]
    while numbers:
        num = numbers.pop(0)
        num_int = int(num)
        
        if l <= num_int <= r:
            answer.append(num_int)
        if len(num) < len(str(r)):
            numbers.append(num + "0")
            numbers.append(num + "5")
    return answer if answer else [-1]