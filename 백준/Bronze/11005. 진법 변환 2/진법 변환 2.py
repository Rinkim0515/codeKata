n, b = map(int,input().split())

digits = []
while n > 0:
    remainder = n % b
    if remainder < 10:
        digits.append(str(remainder))
    else:
        digits.append(chr(remainder - 10 + 65))
    n //= b
print(''.join(reversed(digits)))