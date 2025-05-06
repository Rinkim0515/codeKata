def solution(polynomial):
    answer1 = polynomial.split(" + ")
    answer2 = [0, 0]
    
    for i in answer1:
        if "x" in i:
            if i == "x":
                answer2[0] += 1
            else:
                answer2[0] += int(i[:-1])
        else:
            answer2[1] += int(i)

    if answer2[0] and answer2[1]:
        if answer2[0] == 1:
            return f"x + {answer2[1]}"
        else:
            return f"{answer2[0]}x + {answer2[1]}"
    elif answer2[0]:
        return "x" if answer2[0] == 1 else f"{answer2[0]}x"
    else:
        return str(answer2[1])