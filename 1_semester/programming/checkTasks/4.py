
al = int(input('Введите количество: '))
a = []
print('Начинайте вводить числа')
for i in range(al):
    el = float(input())
    if el < 10:
        el = el* 1.135
    elif el > 10:
        el = el * 0.642
    else: 
        el = el 
    el = round(el, 2)
    a.append(el)

a.sort()

print(a)


save = input('Сохранить в файл? [Y/N]:')
if save.lower() == 'y':
    file = open('4.txt' , 'a')
    file.write(str(a))
    file.close()