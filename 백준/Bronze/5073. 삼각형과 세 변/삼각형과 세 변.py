while True:
    arr = sorted(map(int,input().split()))
    if arr[0] == 0:
        break
    length = len(set(arr))
    if arr[0] + arr[1] <= arr[2]:
        print("Invalid")
    elif length == 3:
        print("Scalene")
    elif length == 2:
        print("Isosceles")
    elif length == 1:
        print("Equilateral")
    