i = input('Введите математическое выражение: ')
try:
    print(eval(i))
except:
    print('Некорректный ввод')