def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    count = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람 태움
        # 무거운 사람은 항상 태움
        right -= 1
        count += 1

    return count