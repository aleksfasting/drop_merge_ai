import random as r
from neural_network import NeuralNetwork
from gameLoop import gameLoop

class tester():
    def __init__(self) -> None: 
        self.nn = NeuralNetwork(49, 2, 49, 49)
        self.nn.createNetwork()
        self.nn.setInputLayer([0] * 49)
        self.nn.pushNetwork()
        self.game = gameLoop()

def main():
    test = tester()


if __name__ == main:
    main()