def solution(myString):
    answer = []
    list = myString.split("x")
    answer = [len(word) for word in list]
            
    return answer