name = input('Введите имя: ')
time = input('Введите время (через двоеточие) ').split(':')
time[0] = int(time[0])
if  0 <= time[0] < 6:
    print('Доброй ночи, ' + name)
elif  6 <= time[0] < 12:
    print('Доброе утро, ' + name)
elif  12 <= time[0] < 17:
    print('Добрый день, ' + name)
elif  17 <= time[0] < 24:
    print('Добрый вечер, ' + name)
else:
    print('Некорректное время')