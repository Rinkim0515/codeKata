def solution(s):
    my_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }
    answer = 0
    for key, value in my_dict.items():
        s = s.replace(key, value)
        
        
    return int(s)