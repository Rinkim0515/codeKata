def solution(spell, dic):
    answer = 2
    count = 0
    for i in range(len(dic)):
        for j in range(len(spell)):
            if spell[j] in dic[i]:
                count += 1
            
        if count == len(spell):
            answer = 1
            break
        else:
            count = 0
        
            
            
    return answer