def inputMatrix():
    print('\n')
    size = input('Введите размерность матрицы через пробел: ').split()
    size[0] = int(size[0])
    size[1] = int(size[1])
    matrix = []
    print('Построчно вводите элементы матрицы через пробел')
    for i in range(size[0]):
        f = False
        while not f:
            r = input().split()
            s = True
            for i in range(len(r)):
                try:
                    r[i] = int(r[i])
                except:
                    s = False 
            if len(r) != size[1] or s == False:
                print('Неправильный ввод. Повторите еще раз')
            else:
                f = True
                matrix.append(r)
    print("\n")
    return matrix

def printMatrix(m):
    print('Результат:')
    for i in m:
        print(*i)
