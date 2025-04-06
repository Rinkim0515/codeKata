def solution(chicken):
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        new = coupon // 10
        answer += new
        coupon = new + (coupon % 10)
    
    return answer