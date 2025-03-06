def solution(binomial):
    answer = 0
    if "+" in binomial:
        list = binomial.split("+")
        return int(list[0]) + int(list[-1])
    elif "-" in binomial:
        list = binomial.split("-")
        return int(list[0]) - int(list[-1])
    elif "*" in binomial:
        list = binomial.split("*")
        return int(list[0]) * int(list[-1])
    return answer