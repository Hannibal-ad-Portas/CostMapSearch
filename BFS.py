# This is an implimentation of breath first search

from queue import *
from Graph import *

def breadthFirstS (Graph, start, goal):
    frontier = Queue()
    startNode = (next((node for node in Graph.nodes if node.position == start), None))
    frontier.put(startNode)
    path = []

    while not frontier.empty():
        current = frontier.get()

        if current.position == goal:
            parentNode = current
            while parentNode != startNode:
                path.append(parentNode.position)
                parentNode = parentNode.parent
            path.reverse()
            return path

        for i, neighbor in enumerate(current.neighbors):
            position = tuple(current.neighbors[i])
            neighborNode = (next((node for node in Graph.nodes if node.position == position), None))
            if neighborNode:
                if not neighborNode.parent:
                    # set parent of the node
                    neighborNode.setParent(current)
                    #path.append(neighborNode.position)
                    frontier.put(neighborNode)
