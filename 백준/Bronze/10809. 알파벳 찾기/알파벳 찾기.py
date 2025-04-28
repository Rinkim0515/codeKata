word = input()
alphabet = [-1] * 26
for i in range(len(word)):
    ch = word[i]
    idx = ord(ch) - ord("a")
    if alphabet[idx] == -1:
        alphabet[idx] = i
print(*alphabet)