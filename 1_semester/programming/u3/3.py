a = input('Введите три числа через пробел ')
a=a.split()
mx = False
for i in a:
    i = int(i)
    if not mx:
        mx = i
    elif i > mx:
        mx = i 
print(mx)

