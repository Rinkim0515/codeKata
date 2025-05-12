def solution(k, tangerine):
    size_count = {}
    for size in tangerine:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    sorted_counts = sorted(size_count.values(), reverse = True)
    total = 0
    answer = 0
    for count in sorted_counts:
        total += count
        answer += 1
        if total >= k:
            break
    return answer