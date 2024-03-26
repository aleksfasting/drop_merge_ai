

class gameTable():
    def __init__(self) -> None:
        self.table = [[0 for i in range(7)] for j in range(7)]

    def __str__(self) -> str:
        s = ''
        for row in self.table:
            s += str(row) + '\n'
        return s
    
    def getElement(self, row: int, column: int) -> int:
        return self.table[i][j]
    
    def dropElement(self, number: int, column: int) -> None:
        if column < 0 or column > 6:
            raise Exception('Invalid column')
        if self.table[6][column] != 0:
            raise Exception('Column is full')
        for i in range(5, -1, -1):
            if self.table[i][column] != 0:
                self.table[i+1][column] = number
                return
        self.table[0][column] = number
    
    def findNeighbours(self, column: int, row: int) -> list[int]:
        left = self.getElement(row, column - 1)
        right = self.getElement(row, column + 1)
        down = self.getElement(row - 1, column)

        return [down, left, right]

    def checkMerge(self, column: int, row: int) -> int:
        """Check if the element can merge with any of its neighbours.
        If no merge: return 0
        If merge down: return 1
        If merge left: return 2
        If merge right: return 3"""
        if column < 0 or column > 6:
            raise Exception('Invalid column')
        if row < 0 or row > 6:
            raise Exception('Invalid row')
        if self.table[6][column] != 0:
            raise Exception('Column is full')
        
        num = self.getElement(row, column)

        neighbours = self.findNeighbours(column, row)

        for i in range(len(neighbours)):
            if num == neighbours[i]:
                return i+1
            
        return 0

    def mergeElements(self, column: int, row: int, neigbourCol: int, neighbourRow: int) -> None:
        num = self.getElement(row, column)
        self.table[neighbourRow][neigbourCol] = 0
        self.table[column][row] = num * 2
