
def er(mx):
    a = [True] * mx 
    for i in range(2, mx):
        if a[i] == True:
            for q in range(i+1, mx):
                if q % i == 0:
                    a[q] = False 

    b = []

    for i in range(1, len(a)):
        if a[i]:
            b.append(i)

    return b 

r = input('Введите диапозон (через пробел) ')
r = r.split()
r[0] = int(r[0])
r[1] = int(r[1])
a = er(r[1])
b = a.copy()
for i in range(0, len(a)):
    if not(a[i] in range(r[0], r[1])):
        b.remove(a[i])

print(b)