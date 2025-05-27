count = int(input()) 
arr = list(map(int, input().split())) 

answer = 0

for i in arr:
    count = 0
    if i != 1:
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:  
            answer += 1

print(answer)