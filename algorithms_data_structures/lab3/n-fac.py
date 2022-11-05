def perm(a, k=0):
    global x
    if k == len(a):
        x += 1
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k + 1)
            a[k], a[i] = a[i], a[k]


x = 0
perm([1, 2, 3, 4, 5])
print(x)