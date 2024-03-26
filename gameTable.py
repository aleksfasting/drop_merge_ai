

class gameTable():
    def __init__(self):
        self.table = [[0 for i in range(7)] for j in range(7)]

    def __str__(self) -> str:
        s = ''
        for i in range(7):
            s += str(self.table) + '\n'
        return s
    
    def getElement(self, i: int, j: int) -> int:
        return self.table[i][j]
        