name = input('Введите имя: ')
sex = input('Введите пол (М/Ж): ')
age = int(input('Введите возраст: '))
sex = sex.upper()

def years(n):
    if 2 <= n <= 4:
        return 'года'
    elif 5 <= n <= 20:
        return "лет"
    elif  2<= (n%10) <= 4:
        return 'года'
    elif n%10==1:
        return 'год'
    else:
        return 'лет'

if sex == 'М':
    print('Его зовут ' + name + '. Ему ' + str(age) + ' ' + years(age))
else:
    print('Ее зовут ' + name + '. Ей ' + str(age) + ' ' + years(age))
