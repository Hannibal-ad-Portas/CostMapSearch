#!/usr/bin/python3
# This program generates a path using several search algorithims

import sys, getopt
from Graph import *
from Grid2Graph import *
from BFS import *

def main (argv):
    grid = grid2Graph ('grid.grd')
    graph = GridGraph (grid[0], grid[1], grid[2])
    graph.setNeighbors()
    start = (0,0)
    goal = (9,9)

    path = breadthFirstS (graph, start, goal)

    print ("Printing Path to Goal")
    print (path)
    #with open('path.txt', 'r') as outfile:
        #outfile.print (path)

main(1)
