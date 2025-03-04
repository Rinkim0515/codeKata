def solution(myString):
    answer = [ word for word in myString.split('x') if word ]
    
    
    return sorted(answer)