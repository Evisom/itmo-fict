data = [141, 196, 14, 152, 203, 14, 165, 179, 46, 42, 154, 126, 123, 25, 210]

a = [0]
b = [0]
c = [0]
d = [0]


for i in range(0, len(data)):
    # print(data[i], data[table[0][-1]])
    if data[i] > data[a[-1]]:
        a.append(i)
    if data[i] > data[b[-1]]:
        b.append(i)
    if data[i] < data[c[-1]]:
        c.append(i)
    if data[i] < data[d[-1]]:
        d.append(i)

print(a)
print(b)
print(c)
print(d)