matrix = [ list(input()) for _ in range(5)]
word = ""
for col in range(15):
    for row in range(5):
        if col >= len(matrix[row]):
            continue
        word += matrix[row][col]
print(word)