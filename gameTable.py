

class gameTable():
    def __init__(self) -> None:
        """Constructor for the table. Initializes the table with 0s."""
        self.table = [[0 for i in range(7)] for j in range(7)]

    def __str__(self) -> str:
        """tostring method for the table"""
        s = ''
        for row in self.table:
            s += str(row) + '\n'
        return s
    
    def getElement(self, row: int, column: int) -> int:
        """getter for a element in the table"""
        if row < 0 or row > 6:
            return 0
        if column < 0 or column > 6:
            return 0
        return self.table[row][column]
    
    def setElement(self, row: int, column: int, number: int) -> None:
        """setter for a element in the table"""
        if column < 0 or column > 6:
            raise Exception('Invalid column')
        if row < 0 or row > 6:
            raise Exception('Invalid row')
        self.table[row][column] = number
    
    def dropElement(self, number: int, column: int) -> None:
        """drops element in a column"""
        if column < 0 or column > 6:
            raise Exception('Invalid column')
        if self.table[6][column] != 0:
            raise Exception('Column is full')
        for i in range(5, -1, -1):
            if self.getElement(i, column) != 0:
                self.setElement(i+1, column, number)
                return
        self.setElement(0, column, number)
        return

    def dropElementFromRow(self, column: int, startRow: int) -> None:
        """drops element from a startrow"""
        if column < 0 or column > 6:
            raise Exception('Invalid column')
        if startRow < 0 or startRow > 6:
            raise Exception('Invalid row')
        for i in range(startRow - 1, -1, -1):
            if self.getElement(i, column) == 0:
                num = self.getElement(startRow, column)
                self.setElement(startRow, column, 0)
                self.setElement(i, column, num)
                return
            
    def dropColumn(self, column: int) -> None:
        """drops every element in a column"""
        if column < 0 or column > 6:
            raise Exception('Invalid column')
        for i in range(6):
            if self.getElement(i, column) != 0:
                self.dropElementFromRow(column, i)
        return
    
    def findNeighbours(self, row: int, column: int) -> list[int]:
        """finds neighbours. Returns a list with the neighbours in the following order: down, left, right. If there is no neighbour in a direction, the value is 0."""
        left = self.getElement(row, column - 1)
        right = self.getElement(row, column + 1)
        down = self.getElement(row - 1, column)

        return [down, left, right]

    def checkMerge(self, row: int, column: int) -> int:
        """Check if the element can merge with any of its neighbours.
        If no merge: return 0
        If merge down: return 1
        If merge left: return 2
        If merge right: return 3
        It will look for a merge in that order."""
        if column < 0 or column > 6:
            raise Exception('Invalid column')
        if row < 0 or row > 6:
            raise Exception('Invalid row')
        if self.table[6][column] != 0:
            raise Exception('Column is full')
        
        num = self.getElement(row, column)
        if num == 0:
            return 0

        neighbours = self.findNeighbours(row, column)

        for i in range(len(neighbours)):
            if num == neighbours[i]:
                return i+1
            
        return 0

    def mergeElements(self, row: int, column: int, neigbourRow: int, neighbourCol: int) -> None:
        """Merge element with its neighbour."""
        num = self.getElement(row, column)
        self.setElement(neigbourRow, neighbourCol, 0)
        self.setElement(row, column, num * 2)

    def mergeLoop(self, row: int, column: int) -> None:
        """Loop for merging the table properly."""
        ret = self.checkMerge(row, column)
        if ret == 0:
            return
        if ret == 1:
            self.mergeElements(row, column, row - 1, column)
            self.dropColumn(column)
            for i in range(6):
                self.mergeLoop(i, column)
            return
        if ret == 2:
            self.mergeElements(row, column, row, column - 1)
            self.dropColumn(column - 1)
            for i in range(6):
                self.mergeLoop(i, column - 1)
            return
        if ret == 3:
            self.mergeElements(row, column, row, column + 1)
            self.dropColumn(column + 1)
            for i in range(6):
                self.mergeLoop(i, column + 1)
            return
        


# Test
t = gameTable()
while True: 
    print(t)

    col = input("Enter column: ")

    if col == 'q':
        break

    t.dropElement(2, int(col))
    for i in range(6):
        t.mergeLoop(i, int(col))

        