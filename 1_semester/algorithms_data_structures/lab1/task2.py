import ioMatrix

def transpose(m):
    new_matrix = []
    for i in range(0, len(m[0])):
        new_matrix.append([])
        for q in range(0,len(m)):
            new_matrix[i].append(m[q][i])
    return new_matrix

def getCollumn(m, index):
    collumn = []
    for i in range(0, len(m)):
        collumn.append(m[i][index])
    return collumn

def multiplication(a, b):
    if len(a[0]) != len(b):
        return False
    new_matrix = []

    for i in range(0,len(a)):
        new_matrix.append([])
        
        for q in range(0, len(b[0])):
            row = a[i]
            collumn = getCollumn(b, q)
            element = 0
            for p in range(0, len(row)):
                element+=row[p]*collumn[p]
            new_matrix[i].append(element) 

    return new_matrix

def rank(matrix):
    matrix_copy = matrix.copy()
    for row in matrix_copy: 
        if row.count(0) == len(row):
            matrix.remove(row)
        
    for r in range(len(matrix)):
        div = 1
        for i in range(len(matrix[r])):
            if matrix[r][i] != 0:
                div = matrix[r][i]
                break
        
        for q in range(len(matrix[r])): 
            matrix[r][q] = matrix[r][q] / div 

        for p in range(r+1, len(matrix)):
            k = matrix[p][i] / matrix[r][i]
            for n in range(len(matrix[p])):
                matrix[p][n] = matrix[p][n] - k*matrix[r][n] 

    matrix_rank = len(matrix)

    for row in matrix:
        if row.count(0) == len(row):
            matrix_rank = matrix_rank - 1
    return matrix_rank


print('Возможные операции с матрицами:')
print('     [1] Транспонирование матрицы')
print('     [2] Умножение матриц')
print('     [3] Определение ранга матриц')
d = input('Что вы хотите сделать? Введите цифру: ')

if d == '1':
    ioMatrix.printMatrix(
        transpose(
        ioMatrix.inputMatrix()
    ))
elif d == '2':
    ioMatrix.printMatrix(
        multiplication(
        ioMatrix.inputMatrix(),
        ioMatrix.inputMatrix()
    ))
elif d == '3':
    print('Ранг матрицы - ', rank(ioMatrix.inputMatrix()))
else:
    print('Неправильный ввод.')