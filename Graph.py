# This file contains a graph class which is a class containing nodes

class Node:
    parent = None
    def __init__(self, row, col, value):
        self.position = [row, col,]
        self.value = value
        self.parent = None
        self.neighbors = []

    def setParent (self, parentPosition):
        self.parent = parentPosition

class GridGraph:
    def __init__(self, width, height, costs):
        self.width  = width
        self.height = height
        self.nodes = []
        for i, row in enumerate(costs):
            for j, col in enumerate(costs[i]):
                self.nodes.append(Node(i, j, costs[i][j]))

    # This method finds all the neighbors of each node and removes the walls
    def setNeighbors (self):
        for node in self.nodes:
            rowP = node.position[0] + 1
            rowM = node.position[0] - 1
            colP = node.position[1] + 1
            colM = node.position[1] - 1

            # if the value is oob remove it
            if (rowP < 0 or rowP >= self.width):
                rowP = None
            if (rowM < 0 or rowM >= self.width):
                rowM = None
            if (colP < 0 or colP >= self.height):
                colP = None
            if (colM < 0 or colM >= self.height):
                colM = None

            # find matching nodes that aren't walls
            tempNode = (next((node for node in self.nodes if node.position == [rowP, node.position[1]]), None))
            if tempNode != None:
                if tempNode.value != 0:
                    node.neighbors.append(tempNode.position)
            tempNode = (next((node for node in self.nodes if node.position == [rowM, node.position[1]]), None))
            if tempNode != None:
                if tempNode.value != 0:
                    node.neighbors.append(tempNode.position)
            tempNode = (next((node for node in self.nodes if node.position == [node.position[0], colP]), None))
            if tempNode != None:
                if tempNode.value != 0:
                    node.neighbors.append(tempNode.position)
            tempNode = (next((node for node in self.nodes if node.position == [node.position[0], colM]), None))
            if tempNode != None:
                if tempNode.value != 0:
                    node.neighbors.append(tempNode.position)

