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
        self.costs = costs
        for i, row in enumerate(costs):
            for j, col in enumerate(costs[i]):
                self.nodes.append(Node(i, j, costs[i][j]))

    # This method finds all the neighbors of each node and removes the walls
    def setNeighbors (self):
        for node in self.nodes:
            row = node.position[0]
            col = node.position[1]
            rowP = row + 1
            rowM = row - 1
            colP = col + 1
            colM = col - 1

            # if the value is out of bounds remove it
            if (rowP < 0 or rowP >= self.width):
                rowP = None
            if (rowM < 0 or rowM >= self.width):
                rowM = None
            if (colP < 0 or colP >= self.height):
                colP = None
            if (colM < 0 or colM >= self.height):
                colM = None

            # find matching nodes that aren't walls
            # Left
            if rowM != None:
                if self.costs[rowM][col] > 0:
                    node.neighbors.append((rowM, col))

            # Right
            if rowP != None:
                if self.costs[rowP][col] > 0:
                    node.neighbors.append((rowP, col))

            # Up
            if colM != None:
                if self.costs[row][colM] > 0:
                    node.neighbors.append((row, colM))

            # Down
            if colP != None:
                if self.costs[row][colP] > 0:
                    node.neighbors.append((row, colP))
