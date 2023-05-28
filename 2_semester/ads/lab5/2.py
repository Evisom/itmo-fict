class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])
        self.array = []
        self.targetMatrixPosition = [-1, -1]

    def __matrixToArray(self):
        for c in range(self.n):
            for r in range(self.m):
                self.array.append(self.matrix[r][c])

    def __binarySearch(self, array, x, low, high):
        if high >= low:
            mid = low + (high - low)//2
            if array[mid] == x:
                return mid
            elif array[mid] > x:
                return self.__binarySearch(array, x, low, mid-1)
            else:
                return self.__binarySearch(array, x, mid + 1, high)
        else:
            return -1

    def search(self, target):
        self.__matrixToArray()
        self.targetArrayPosition = self.__binarySearch(
            self.array, target, 0, len(self.array)-1)
        self.targetMatrixPosition = [
            self.targetArrayPosition//self.m, self.targetArrayPosition % self.m]
        return self.targetMatrixPosition


print(Matrix([
    [0, 6, 10, 16],
    [2, 7, 12, 57],
    [4, 8, 15, 68]]).search(7))

print(Matrix([
    [0, 6, 10, 16],
    [2, 7, 12, 57],
    [4, 8, 15, 68]]).search(15))
