subject = [list(input().split()) for _ in range(20)]
my_dict = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

total_score = 0.0
total_credit = 0.0

for sub in subject:
    grade = sub[2]
    if grade == "P":
        continue
    credit = float(sub[1])
    total_credit += credit
    total_score += credit * my_dict[grade]

avg = total_score / total_credit
print(f"{avg:.6f}")