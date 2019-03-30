# This is an implimentation of breath first search

from queue import *
from Graph import *

def breadthFirstS (Graph, start, goal):
    frontier = Queue()
    startNode = (next((node for node in Graph.nodes if node.position == [start[0], start[1]]), None))
    frontier.put(startNode)
    path = []

    while not frontier.empty():
        current = frontier.get()

        if (current.position[0] == goal[0] and current.position[1] == goal[1]):
            print ("Found goal at")
            print (current.position)
            # call function add parents to path
            path.append(current.position)
            currentParent = current.position
            parentNode = current
            while parentNode != startNode:
                # Get the position of the parent of each node in the path
                parentNode = parentNode.parent
                currentParent = parentNode.position
                print (currentParent)
                path.append(currentParent)
            return path

        for neighbor in current.neighbors:
            neighborNode = (next((node for node in Graph.nodes if node.position == [neighbor[0], neighbor[1]]), None))
            if neighborNode != None:
                if neighborNode.parent == None:
                    # set parent of the node
                    neighborNode.setParent(current)
                    #path.append(neighborNode.position)
                    frontier.put(neighborNode)
