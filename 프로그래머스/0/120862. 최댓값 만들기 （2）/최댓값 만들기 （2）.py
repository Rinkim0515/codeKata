def solution(numbers):
    answer = len(numbers)
    numbers.sort()
    case1 = numbers[0] * numbers[1] 
    case2 = numbers[answer - 1] * numbers[answer - 2] 
    return case1 if case1 > case2 else case2