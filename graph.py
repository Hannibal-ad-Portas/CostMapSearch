# This file contains a graph class

class GridGraph:
    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        self.obsticals = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.columns and 0 <= y < self.rows

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
