# This is a non recursive implementation of a Depth First Search

from queue import *
from Graph import *

def depthFirstS (Graph, start, goal):
    frontier = []
    startNode = (next((node for node in Graph.nodes if node.position == start), None))
    frontier.append(startNode)
    path = []

    while frontier:
        current = frontier.pop()

        # Early Exit implementation
        if (current.position == goal):
            # add parents to path
            parentNode = current
            while parentNode != startNode:
                path.append(parentNode.position)
                parentNode = parentNode.parent
            path.reverse()
            return path

        # check to see if the node has been visited
        if current.visited == False:
            current.visited = True
            # set parent of the node
            for neighbor in current.neighbors:
                position = tuple(neighbor)
                neighborNode = (next((node for node in Graph.nodes if node.position == position ), None))
                if neighborNode:
                    if (neighborNode.visited == False):
                        neighborNode.setParent(current)
                        frontier.append(neighborNode)
