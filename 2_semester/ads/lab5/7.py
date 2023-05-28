from random import randrange

a = [randrange(-100, 100) for i in range(20)]
ans = 10000000000
mn = min(a)
mx = max(a)
b = []
d = dict()
for el in a:
    d[el] = 1
for i in range(len(a)):
    if a[i] != mn and a[i] != mx:
        b.append(a[i]-1)
        b.append(a[i]+1)
    elif a[i] == mn:
        b.append(a[i]+1)
    else:
        b.append(a[i]-1)
for el in b:
    if el not in d:
        ans = min(ans, el)
print("Наименьшее пропущенное целое: " + str(ans))
print(a)
