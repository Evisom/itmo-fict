import os


class TicTacToe:
    def __init__(self, *map):
        self.empty = 0
        self.map = map or [
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty]
        ]
        self.symbols = ['_', 'X', 'O']
        self.figures = [1, 2]
        self.winner = None

    def makeMove(self, fig, cellY, cellX):
        if cellY in range(0, 3) and cellX in range(0, 3):
            if self.map[cellY][cellX] == self.empty:
                print(cellY, cellX)
                self.map[cellY][cellX] = fig
                self.__checkWin()
            else:
                print('Cell already taken!')
        else:
            print('Invalid input!')

    def resetMap(self, fig):
        self.map = [[self.empty]*3] * 3

    def printMap(self, fig):
        os.system('cls||clear')
        print(game.winner)
        print(self.symbols[fig], ' move!')

        print('  \  0 1 2', end='')
        for r in range(len(self.map)):
            print('\n' + str(r) + ' | ', end=' ')
            for c in self.map[r]:
                print(self.symbols[c], end=' ')

        print('\n\n')

    def __checkWin(self):
        for i in range(len(self.map)):
            for f in self.figures:
                if self.map[0][i] == self.map[1][i] == self.map[2][i] == f:
                    self.winner = f
                    return
                if self.map[i][0] == self.map[i][1] == self.map[i][2] == f:
                    self.winner = f
                    return
        for f in self.figures:
            if self.map[0][0] == self.map[1][1] == self.map[2][2] == f:
                self.winner = f
                return
            if self.map[0][2] == self.map[1][1] == self.map[2][0] == f:
                self.winner = f
                return


game = TicTacToe()

i = 0
while not (game.winner) and i < 9:
    fig = game.figures[i % 2]
    game.printMap(fig)
    cell = input('Enter X, Y of the cell:').split()
    try:
        cell[0] = int(cell[0])
        cell[1] = int(cell[1])
        game.makeMove(fig, cell[1], cell[0])
        i += 1
    except:
        print('Invalid input')


game.printMap(fig)
if game.winner:
    print('Game winnder - ', game.symbols[game.winner])
else:
    print('Draw')
