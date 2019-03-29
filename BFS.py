# This is an implimentation of breath first search

from queue import *
from Graph import *

def breadthFirstS (Graph, start, goal):
    frontier = Queue()
    startNode = (next((node for node in Graph.nodes if node.position == [start[0], start[1]]), None))
    frontier.put(startNode)
    path = []
    path.append(startNode.position)

    while not frontier.empty():
        current = frontier.get()

        if (current.position[0] == goal[0] and current.position[1] == goal[1]):
            print ("Found goal at")
            print (current.position)
            return path

        for neighbor in current.neighbors:
            neighborNode = (next((node for node in Graph.nodes if node.position == [neighbor[0], neighbor[1]]), None))
            if neighborNode != None:
                if neighborNode.position not in path:
                    path.append(neighborNode.position)
                    frontier.put(neighborNode)
                    neighborNode.setParent(current.position)
