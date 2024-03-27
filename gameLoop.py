from gameTable import gameTable

class gameLoop():
    def __init__(self) -> None:
        """Constructor for the game loop"""
        self.table = gameTable()

    def loop(self):
        """Main loop for the game"""
        while True:
            number = 2
            print(self.table)
            try:
                column = input('Enter column: ')
                if column == 'q':
                    break
                column = int(column)
            except Exception as e:
                print(e)
                continue

            self.table.dropElement(number, column)
            for i in range(6):
                self.table.mergeLoop(i, column)
            print(self.table)

    def loopAI(self, column: int, number: int) -> gameTable:
        """Main loop for the game with AI"""
        try:
            self.table.dropElement(number, column)
            for i in range(6):
                self.table.mergeLoop(i, column)
        except Exception as e:
            if str(e) == 'Column is full':
                return False
            print(e)
        return self.table