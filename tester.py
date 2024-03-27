import random as r
from neural_network import NeuralNetwork
from gameLoop import gameLoop

class tester():
    def __init__(self) -> None: 
        self.nn = NeuralNetwork(49, 2, 30, 7)
        self.nn.createNetwork()
        self.nn.setInputLayer([0] * 49)
        self.nn.pushNetwork()
        self.game = gameLoop()

    def testLoop(self) -> None:
        number = 2
        while True:
            column = self.nn.getMaxOutput()
            table = self.game.loopAI(column, number)
            if table == False:
                break
            self.nn.setInputLayer([table.getElement(i, j) for i in range(7) for j in range(7)])

def main() -> None:
    print("Starting test...")
    test = tester()
    number = 2

    test.testLoop()

    print(test.game.table)

if __name__ == '__main__':
    main()