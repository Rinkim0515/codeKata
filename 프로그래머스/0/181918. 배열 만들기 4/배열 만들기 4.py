def solution(arr):
    stk = []
    for idx in arr: 
        while stk and stk[-1] >= idx:
            stk.pop()
        
        stk.append(idx)

    return stk