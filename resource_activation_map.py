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
