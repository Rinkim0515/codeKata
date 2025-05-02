word = input()
dict = ["c=", "c-", "dz=", "d-", "lj",	"nj", "s=","z="]
a = 0
c = 0

while c < len(word):
    if word[c:c+3] == "dz=":
        c += 3     
        a += 1
    elif word[c:c+2] in dict:
        c += 2
        a += 1
    else:
        c += 1
        a += 1
print(a)        