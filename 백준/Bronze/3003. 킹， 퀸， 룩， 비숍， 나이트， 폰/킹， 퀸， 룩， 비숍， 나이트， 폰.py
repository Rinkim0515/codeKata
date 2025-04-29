chess = [1, 1, 2, 2, 2, 8]
have = list(map(int,input().split()))

for i in range(len(chess)):
    chess[i] -= have[i]
print(*chess)
