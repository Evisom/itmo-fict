flag = True 

def calc(a, b, c):
    d = b**2 - 4 * a * c 
    if a == 0:
        return "a должно быть больше нуля"
    if d < 0:
        return('Нет корней')
    elif d == 0:
        x_1 = ((-1)*b)/(2*a)
        return(x_1)
    else: 
        x_1 = ((-1)*b + (d)**(1/2) )/(2*a)
        x_2 = ((-1)*b - (d)**(1/2) )/(2*a)
        return(x_1, x_2)

while flag:
    i = input('Введите коэффиценты уравнения, через запятую: ')
    if i.lower() == 'q':
        flag = False
        break 
    i = i.split()
    if len(i) != 3:
        print('Неправильный ввод!')
    else:
        try:
            a = int(i[0])
            b = int(i[1])
            c = int(i[2])
            print(calc(a,b,c))
        except:
            print('Некорректный ввод!')
        
        