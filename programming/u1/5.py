s = int(input("Введите число: "))
m = s//60
s = s%60
h = m//60
m = m%60
d = h//24
h = h%24
print(str(d) + ":" + str(h) + ":" + str(m) + ":" + str(s))
