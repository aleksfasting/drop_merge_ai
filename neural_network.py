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
        self.outs.append(Edge(node, 0))

    def getValue(self) -> int:
        """Getter for the value of the node."""
        return self.value
    
    def setValue(self, value) -> None:
        """Setter for the value of the node."""
        self.value = value

    def getOuts(self) -> list[Edge]:
        """Getter for the outs of the node."""
        return self.outs



class NeuralNetwork():

    def __init__(self, columns: int, hiddenLayers: int, nodesInLayer: int, outputs: int):
        """Constructor for the neural network. Initializes the network with the given parameters."""
        self.inputs = columns
        self.outputs = outputs
        self.layers = hiddenLayers
        self.nodesInLayer = nodesInLayer
        self.inputLayer = []
        self.hiddenLayer = []
        self.outputLayers = [[] for i in range(self.nodesInLayer)]

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
            if layer == self.nodesInLayer - 1:
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
