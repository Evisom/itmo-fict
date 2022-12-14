labyrinth = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def printMatrix(matrix):
    for row in matrix:
        print(*row)

start_cell = [7,0]

def search(a, cell, visited):
    if 0 <= cell[0] < len(a) and 0 <= cell[1] < len(a[0]):
        if a[cell[0]][cell[1]] == 1:
            return False 
        if cell not in visited:
            visited.append(cell)

            if cell[1] == len(a[0]) - 1:
                return(visited)
            else:
                a[cell[0]][cell[1]] = '*'
                return \
                search(a, [cell[0], cell[1]+1], visited) or \
                search(a, [cell[0]+1, cell[1]], visited) or \
                search(a, [cell[0]-1, cell[1]], visited) or \
                search(a, [cell[0], cell[1]-1], visited)
                

v = (search(labyrinth, start_cell, []))

for i in v:
    labyrinth[i[0]][i[1]] = "\033[93m*\033[0m"

printMatrix(labyrinth)