

class gameTable():
    def __init__(self) -> None:
        self.table = [[0 for i in range(7)] for j in range(7)]

    def __str__(self) -> str:
        s = ''
        for row in self.table:
            s += str(row) + '\n'
        return s
    
    def getElement(self, i: int, j: int) -> int:
        return self.table[i][j]
    
    def dropElement(self, number: int, column: int) -> None:
        for i in range(6, -1, -1):
            if self.table[i][column] != 0:
                self.table[i+1][column] = number
                return
