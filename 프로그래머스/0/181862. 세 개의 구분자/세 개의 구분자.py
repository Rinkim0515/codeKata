def solution(myStr):
    answer = []
    string = ""
    for idx,val in enumerate(myStr):
        if val in "abc":
            if string != "":
                answer.append(string)
                string = ""
            continue
        
        else:
            string += val
    if string != "":
        answer.append(string)
    return ["EMPTY"] if answer == [] else answer