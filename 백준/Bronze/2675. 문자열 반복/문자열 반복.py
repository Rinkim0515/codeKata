count = int(input())

for i in range(count):
    answer = ""
    a, b = input().split()
    for i in b:
        answer += i * int(a)
    print(answer)
        
    