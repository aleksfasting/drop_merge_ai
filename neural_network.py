class Edge():
    def __init__(self, node, w: int) -> None:
        self.weight = w
        self.node = node
    
    def getWeight(self) -> int:
        return self.weight
    
    def setWeight(self, w: int) -> None:
        self.weight = w
    
    def getNode(self):
        return self.node


class Node():

    def __init__(self) -> None:
        """Constructor for the node. Initializes the node with 0 value and no outs."""
        self.value = 0
        self.outs = []

    def addOut(self, node) -> None:
        """Adds an out to the node."""
        self.outs.append(Edge(node, 1))

    def getValue(self) -> int:
        """Getter for the value of the node."""
        return self.value
    
    def setValue(self, value) -> None:
        """Setter for the value of the node."""
        self.value = value

    def getOuts(self) -> list[Edge]:
        """Getter for the outs of the node."""
        return self.outs
    
    def pushValue(self) -> None:
        """Pushes the value of the node to the outs. This function assumes the output node been reset since last use"""
        for edge in self.outs:
            edge.getNode().setValue(edge.getNode().getValue() + self.getValue() * edge.getWeight())


class NeuralNetwork():

    def __init__(self, columns: int, hiddenLayers: int, nodesInLayer: int, outputs: int):
        """Constructor for the neural network. Initializes the network with the given parameters."""
        self.inputs = columns
        self.outputs = outputs
        self.layers = hiddenLayers
        self.nodesInLayer = nodesInLayer
        self.inputLayer = []
        self.hiddenLayer = [[] for i in range(self.layers)]
        self.outputLayer = []

    def addInputLayer(self):
        """Adds the input layer to the network. Cannot be called before addHiddenLayer() is called."""
        for i in range(self.inputs):
            self.inputLayer.append(Node())
            self.inputLayer[i].setValue(0)
            for j in range(self.nodesInLayer):
                self.inputLayer[i].addOut(self.hiddenLayer[0][j])

    def addHiddenLayer(self, layer: int):
        """Adds hidden layers to the network. Cannot be called before addOutputLayer() is called."""
        for i in range(self.nodesInLayer):
            self.hiddenLayer[layer].append(Node())
            self.hiddenLayer[layer][i].setValue(0)
            if layer == self.layers - 1:
                for j in range(self.outputs):
                    self.hiddenLayer[layer][i].addOut(self.outputLayer[j])
            else:
                for j in range(self.nodesInLayer):
                    self.hiddenLayer[layer][i].addOut(self.hiddenLayer[layer+1][j])

    def addOutputLayer(self):
        """Adds the output layer to the network."""
        for i in range(self.outputs):
            self.outputLayer.append(Node())
            self.outputLayer[i].setValue(0)

    def setInputLayer(self, inputs: list[int]) -> None:
        """Pushes the inputs to the hidden layer."""
        for i in range(self.inputs):
            self.inputLayer[i].setValue(inputs[i])

    def pushInputLayer(self) -> None:
        """Pushes the input layer to the hidden layer."""
        for node in self.inputLayer:
            node.pushValue()

    def pushHiddenLayer(self, layer: int) -> None:
        """Pushes the hidden layer to the next hidden layer."""
        for node in self.hiddenLayer[layer]:
            node.pushValue()

    def getMaxOutput(self) -> int:
        """Returns the index of the output node with the highest value."""
        maxIndex = 0
        for i in range(self.outputs):
            if self.outputLayer[i].getValue() > self.outputLayer[max].getValue():
                maxIndex = i
        return maxIndex
    
    def __str__(self):
        """tostring method for the neural network"""
        s = ''
        s += 'Input layer:\n'
        for node in self.inputLayer:
            s += str(node.getValue()) + ' '
        s += '\n'
        for i in range(self.layers):
            s += 'Hidden layer ' + str(i) + ':\n'
            for node in self.hiddenLayer[i]:
                s += str(node.getValue()) + ' '
            s += '\n'
        s += 'Output layer:\n'
        for node in self.outputLayer:
            s += str(node.getValue()) + ' '
        s += '\n'
        return s
    
    def createNetwork(self) -> None:
        """Adds layers to the network."""
        self.addOutputLayer()
        for i in range(self.layers-1, -1, -1):
            self.addHiddenLayer(i)
        self.addInputLayer()

    def pushNetwork(self) -> None:
        """Pushes the network."""
        self.pushInputLayer()
        for i in range(self.layers):
            self.pushHiddenLayer(i)

def main():
    nn = NeuralNetwork(7, 2, 10, 7)
    nn.createNetwork()
    nn.setInputLayer([1, 2, 3, 4, 5, 6, 7])
    nn.pushNetwork()
    print(nn)

if __name__ == '__main__':
    main()