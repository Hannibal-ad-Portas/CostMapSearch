import math
import time
from PriorityQueue import *
from Graph import *

def heuristic(a, b, heur):
    D = 1 #base cost to move to a square from a neighbor
    (x1, y1) = a
    (x2, y2) = b

    if (heur == "manhattan"):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return D * (dx + dy)

    if (heur == "euclidean"):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return D * math.sqrt(dx * dx + dy * dy)

    if (heur == "zero"):
        return 0

def aStar (Graph, start, goal, heur):
    frontier = PriorityQueue();
    startNode = (next((node for node in Graph.nodes if node.position == start), None))
    frontier.put(startNode, 0)
    visitedNodes = []
    currentCost = {}
    currentCost[start] = 0
    path = []

    while not frontier.empty():
        current = frontier.get()
        print("Examining node at:", current.position)

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
                newCost = currentCost[tuple(current.position)] + neighborNode.cost
                neighborPosition = tuple(neighborNode.position)
                if neighborPosition not in currentCost or newCost < currentCost[neighborPosition]:
                    currentCost[neighborPosition] = newCost
                    dist2Goal = heuristic(goal, neighbor, heur)
                    print ("Heuristic: ", dist2Goal)
                    print ("Cost: ", newCost)
                    priority = newCost + dist2Goal
                    print("Priority:", priority)
                    frontier.put(neighborNode, priority)
                    neighborNode.setParent(current)
        time.sleep(.25)
