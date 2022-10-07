n = int(input('Введите порядковый номер месяца: '))
z = {1,2,12}
v = {3,4,5}
l = {6,7,8}
o = {9,10,11}
if n in z:
    print('Зима')
elif n in v:
    print('Весна')
elif n in l:
    print('Лето')
elif n in o:
    print('Осень')
else:
    print('Некорректный номер')