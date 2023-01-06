from random import randint as r
s = []
for i in range(20):
    s.append(r(1, 150))
print(s)
i = 0
c = 0
while i != len(s):
    if s[i-1] > s[i]:
        s[i-1], s[i] = s[i], s[i-1]
        c += i + 1
        i = 1
    else:
        i += 1
print(s)