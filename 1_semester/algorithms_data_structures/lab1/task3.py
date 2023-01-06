import numpy as np
import ioMatrix

print('Возможные операции с матрицами:')
print('     [1] Транспонирование матрицы')
print('     [2] Умножение матриц')
print('     [3] Определение ранга матриц')
d = input('Что вы хотите сделать? Введите цифру: ')

if d == '1':
    ioMatrix.printMatrix(
        np.array(ioMatrix.inputMatrix()).T
    )
elif d == '2':
    ioMatrix.printMatrix(
        np.dot(
        np.array(ioMatrix.inputMatrix()),
        np.array(ioMatrix.inputMatrix())
    ))
elif d == '3':
    print('Ранг матрицы - ', np.linalg.matrix_rank(ioMatrix.inputMatrix()))
else:
    print('Неправильный ввод.')

