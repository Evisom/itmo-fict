from random import randrange
n = int(input("Введите количество чисел: "))
a = [randrange(-100, 100) for i in range(n)]
print(a)

f = [1]*n
for i in range(1, n):
    if a[i] > a[i-1]:
        f[i] = f[i-1]+1
print("Длина: "+str(max(f)))        
