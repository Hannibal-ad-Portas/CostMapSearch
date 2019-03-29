# This function takes a .grd file and creadtes a graph object out of it.
# The function takes the file, ignores the first line, and places the move costs
# into a list of lists of the same height and width as the image the .grd file was
# created from

from Graph import *

def grid2Graph (gridFile):
    costs = []
    with open(gridFile, 'r') as grid:
        # get the contents of the first line and strip trailing new line character
        firstLine = grid.readline().strip()
        for line in grid:
            costs.append(line.strip())

    for i, item in enumerate(costs):
        costs[i] = item.split(' ')
        for j, num in enumerate(costs[i]):
            costs[i][j] = float(costs[i][j])

    rows, cols = firstLine.split(' ')
    rows = int(rows)
    cols = int(cols)

    return rows, cols, costs
