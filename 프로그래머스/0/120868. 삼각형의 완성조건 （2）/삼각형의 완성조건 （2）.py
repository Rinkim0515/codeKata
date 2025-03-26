def solution(sides):
    sides.sort()
    small, big = sides[0], sides[1]
    count1 = (small + big -1) - big
    count2 = big - (big - small)
    return count1 + count2