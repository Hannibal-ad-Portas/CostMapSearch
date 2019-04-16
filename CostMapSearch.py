#!/usr/bin/python3
# This program generates a path using several search algorithims
__author__ = "James Conroy"

import sys
from Graph import *
from Grid2Graph import *
from BFS import *
from DFS import *
from AStar import *

def usage (argv):
    print("Usage:")
    print('\t',str(sys.argv[0]), "method, grid.txt, rstart. cstart, rend, cend, path.txt")
    print("Methods:")
    print("\tBFS\n\tDFS\n\tAStarZero\n\tAStarManhattan\n\tAStarEuclidean")

def main (argv):

    if (len(sys.argv) != 8):
        print("You have the wrong number of arguments")
        usage(argv)
        return

    method = str(sys.argv[1])
    inFile = str(sys.argv[2])
    rstart = int(sys.argv[3])
    cstart = int(sys.argv[4])
    rend = int(sys.argv[5])
    cend = int(sys.argv[6])
    outFile = str(sys.argv[7])

    grid = grid2Graph (inFile)
    graph = GridGraph (grid[0], grid[1], grid[2])
    graph.setNeighbors()
    start = (rstart, cstart)
    goal = (rend, cend)

    if (method == "DFS"):
        path = depthFirstS (graph, start, goal)
    elif (method == "BFS"):
        path = breadthFirstS (graph, start, goal)
    elif (method == "AStarZero"):
        path = aStar (graph, start, goal, "zero")
    elif (method == "AStarManhattan"):
        path = aStar (graph, start, goal, "manhattan")
    elif (method == "AStarEuclidean"):
        path = aStar (graph, start, goal, "euclidean")
    else:
        print("Method not Reconised")
        usage(argv)
        return

    if path:
        print ("Printing Path to Goal")
        with open(outFile, 'w') as pathFile:
            for p, point in enumerate(path):
                pathFile.write(' '.join([str(i) for i in path[p]]))
                pathFile.write('\n')
    else:
        print ("No path found")

main(1)
