word = input().upper()
my_dict = {}
for i in word:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
max_count = max(my_dict.values())
most_common = [k for k, v in my_dict.items() if v == max_count]

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])           