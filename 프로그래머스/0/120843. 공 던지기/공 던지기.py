def solution(numbers, k):
    answer = 0
    index = ((k - 1) * 2) % len(numbers)
    return numbers[index]