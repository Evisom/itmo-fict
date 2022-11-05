s = [3, 4, 5, 2]
for i in range(len(s)):
    a = s[i]
    for j in range(3):
        s[i] *= a
print(s)