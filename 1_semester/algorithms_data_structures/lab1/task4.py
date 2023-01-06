import ioMatrix
import numpy as np
import timeit

test = [
    [4,3,2],
    [2,1,-1],
    [3,3,2]
]
def det(m):
    d = m[0][0]*m[1][1]*m[2][2]+\
        m[2][0]*m[0][1]*m[1][2]+\
        m[1][0]*m[2][1]*m[0][2]-\
        m[2][0]*m[1][1]*m[0][2]-\
        m[0][0]*m[2][1]*m[1][2]-\
        m[1][0]*m[0][1]*m[2][2]
    return d
        

def reverse(matrix):
    d = det(matrix)
    if d == 0:
        print('Обратная матрица невозможна, определитель равен нулю!')
        return
    new_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    k = 1
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            a = []
            for q in range(len(matrix)):
                for p in range(len(matrix[q])):
                    if m != p and n != q:
                        a.append(matrix[q][p])
            new_matrix[m][n] = (a[0] * a[3] - a[1] * a[2]) * k
            k = k*(-1)

    for n in range(len(new_matrix)):
        for m in range(len(new_matrix[n])):
            new_matrix[n][m] = round(new_matrix[n][m] * (1/d), 15)

    return new_matrix



print('Возведение матрицы в степень -1: ')
inp = ioMatrix.inputMatrix()
ioMatrix.printMatrix(reverse(inp))

start_time = timeit.default_timer()
reverse(inp)
time1 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
np.linalg.inv(inp)
time2 = timeit.default_timer() - start_time

print('\n')
print('Время выполнения моего алгоритма - ', time1, ' секунд.')
print('Время выполнения с использованием numpy - ', time2, ' секунд.')
print('Алгоритм с использованием numpy выполнился быстрее в ', round(time2/time1, 2), ' раз')
