import numpy as np

A = np.diag([1, 2, 3, 4])
B = np.diag([5, 6, 7, 8])
C = np.diag([9, 10, 11, 12])
D = np.diag([13, 14, 15, 16])

m = [A, B, C, D]


def strassen(A, B):
    n = A.shape[0]
    if n <= 2:
        return np.dot(A, B)
    else:
        # Разбиваем матрицы на подматрицы одинакового размера
        n2 = n // 2
        A11 = A[:n2, :n2]
        A12 = A[:n2, n2:]
        A21 = A[n2:, :n2]
        A22 = A[n2:, n2:]
        B11 = B[:n2, :n2]
        B12 = B[:n2, n2:]
        B21 = B[n2:, :n2]
        B22 = B[n2:, n2:]

        # Рекурсивно вычисляем произведение подматриц
        P1 = strassen(A11 + A22, B11 + B22)
        P2 = strassen(A21 + A22, B11)
        P3 = strassen(A11, B12 - B22)
        P4 = strassen(A22, B21 - B11)
        P5 = strassen(A11 + A12, B22)
        P6 = strassen(A21 - A11, B11 + B12)
        P7 = strassen(A12 - A22, B21 + B22)

        # Вычисляем промежуточные матрицы и результирующую матрицу
        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 + P3 - P2 + P6
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

        return C

matrix = []
for i in range(0, len(m)-1):
    if len(matrix) == 0:
        matrix = strassen(m[i], m[i+1])
    else:
        matrix = strassen(matrix, m[i+1])

print(matrix)
print(np.dot(np.dot(m[0], m[1]), np.dot(m[2], m[3])))
