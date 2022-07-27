# Make a hex class that can go in a coordinate system, with attributes to
# include: region, roll values, value positions (between hexes on the
# intersections -- might take a conversion between the hex coordinate and the
# intersection coordinate). Solve a map with defined regions, and give the
# roll values and their positions for the map to work, given a desired number
# of hexes with specified roll values in each region.

import numpy as np

class Hex:

    def __init__(self):
        self.region = "Forest" # Should set the region on creation of the hex object
        self.valnoon = 0 # These are the roll values and their positions on a clock (noon is up)
        self.val2 = 0
        self.val4 = 0
        self.val6 = 0
        self.val8 = 0
        self.val10 = 0
        self.location = (0, 0)    # Hex grid coordinates
        self.neighborNE = (0, 0)
        self.neighborE = (0, 0)
        self.neighborSE = (0, 0)
        self.neighborSW = (0, 0)
        self.neighborW = (0, 0)
        self.neighborNW = (0, 0)
        self.calc_neighbors()

    def calc_neighbors(self):
        # Calculate the coordinates of the neighbor hexes
        self.neighborNE = (self.location[0] + 1, self.location[1] - 1)
        self.neighborE = (self.location[0] + 1, self.location[1])
        self.neighborSE = (self.location[0], self.location[1] + 1)
        self.neighborSW = (self.location[0] - 1, self.location[1] + 1)
        self.neighborW = (self.location[0] - 1, self.location[1])
        self.neighborNW = (self.location[0], self.location[1] - 1)
