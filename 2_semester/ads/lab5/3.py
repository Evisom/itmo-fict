from itertools import permutations


class Chess:
    def __init__(self, map=None):
        if map == None:
            self.map = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]

        else:
            self.map = map

    def printMap(self, hideOnes=False):
        for i in self.map:
            for q in i:
                if hideOnes:
                    if q == 1:
                        print(0, end=' ')
                    else:
                        print(q, end=' ')
                else:
                    print(q, end=' ')
            print('', end='\n')

    def diag(self, x, y, p, q):
        if x+p in range(0, 8) and y+q in range(0, 8):
            if self.map[y+q][x+p] == 0:
                self.map[y+q][x+p] = 1
            self.diag(x+p, y+q, p, q)
        else:
            return

    def placeFig(self, x, y):
        if self.map[y][x] == 0:
            for i in range(8):
                if self.map[i][x] == 0:
                    self.map[i][x] = 1
                if self.map[y][i] == 0:
                    self.map[y][i] = 1
            self.diag(x, y, 1, 1)
            self.diag(x, y, 1, -1)
            self.diag(x, y, -1, 1)
            self.diag(x, y, -1, -1)
            self.map[y][x] = 2
            return self.map
        else:
            return 0


combs = set(permutations([0, 1, 2, 3, 4, 5, 6, 7], 8))

c = 0
for i in combs:
    m = Chess()
    w = True
    for q in range(len(i)):
        r = m.placeFig(q, int(i[q]))
        if r == 0:
            w = False
            break
    if w:
        c += 1
        print()
        m.printMap(True)
        print()

print(c)
