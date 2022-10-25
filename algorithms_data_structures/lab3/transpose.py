def transpose(m):
    c = 1
    new_matrx = []
    c+=2
    for i in range(0, len(m)):
        new_matrx.append([])
        c+=2
        for q in range(0, len(m[i])):
            c+=4
            new_matrx[i].append(m[q][i])
    print('Количество шагов:', c+1)
    return new_matrx

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

def printMatrix(m):
    for i in m:
        print(*i)

printMatrix(matrix)
printMatrix(transpose(matrix))
