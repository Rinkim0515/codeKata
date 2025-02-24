def solution(a, b, c, d):
    numbers = [a, b, c, d]
    unique_numbers = set(numbers)

    if len(unique_numbers) == 1:
        return a * 1111

    elif len(unique_numbers) == 2:
        for num in unique_numbers:
            if numbers.count(num) == 3:
                p, q = num, [x for x in unique_numbers if x != num][0]
                return (10 * p + q) ** 2
            elif numbers.count(num) == 2:
                p, q = unique_numbers
                return (p + q) * abs(p - q)

    elif len(unique_numbers) == 3:
        for num in unique_numbers:
            if numbers.count(num) == 2:
                p = num
        q, r = [x for x in unique_numbers if x != p]
        return q * r  # q × r

    else:
        return min(numbers)