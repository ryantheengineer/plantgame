# combattest.py: Testing combat bidding mechanism, especially statistical
# analysis of lots of test runs

import numpy as np
import random as rd

# Class for an individual faction in a battle. Inputs include available
# bidding power, as well as a strategy (split even, high/low, low/high,
# all/nothing, random split)
class Faction:
    # Initialize the class instance
    def __init__(self, bidpower, strategy):
        self.bidpower = bidpower
        self.strategy = strategy

    def get_bid_strategy(self, argument):
        # Make a bid based on the chosen strategy
        """Dispatch Method"""
        method_name = '_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid bid strategy")
        # Call the method as we return it
        return method()

    def _evensplit(self):
        # Split bidpower evenly among bids. If bidpower is odd, randomly choose
        # which bid to add 1 to
        if self.bidpower % 2 == 1:
            x = random()
            if x > 0.5:
                waterbid = self.bidpower // 2 + 1
                nutrientbid = self.bidpower - waterbid
            else:
                nutrientbid = self.bidpower // 2 + 1
                waterbid = self.bidpower - nutrientbid
        else:
            waterbid = self.bidpower // 2
            nutrientbid = waterbid

        return [waterbid, nutrientbid]

    def _highwater(self):
        # Go 2/3 power on water, 1/3 power on nutrients. Always add additional
        # power from remainders onto the high bid
        if self.bidpower % 3 != 0:
            waterbid = (2* self.bidpower // 3) + (self.bidpower % 3)
            nutrientbid = self.bidpower - waterbid
        else:
            waterbid = 2 * self.bidpower // 3
            nutrientbid = self.bidpower // 3

        return [waterbid, nutrientbid]

    def _highnutrient(self):
        # Go 1/3 power on water, 2/3 power on nutrients. Always add additional
        # power from remainders onto the high bid
        if self.bidpower % 3 != 0:
            nutrientbid = (2* self.bidpower // 3) + (self.bidpower % 3)
            waterbid = self.bidpower - waterbid
        else:
            nutrientbid = 2 * self.bidpower // 3
            waterbid = self.bidpower // 3

        return [waterbid, nutrientbid]

    def _allwater(self):
        # Put full bidding power on water
        waterbid = self.bidpower
        nutrientbid = 0

        return [waterbid, nutrientbid]

    def _allnutrient(self):
        # Put full bidding power on nutrients
        waterbid = 0
        nutrientbid = self.bidpower

        return [waterbid, nutrientbid]

    def _randomsplit(self):
        waterbid = rd.randint(0,self.bidpower)
        nutrientbid = self.bidpower - waterbid

        return [waterbid, nutrientbid]



# Take a number of factions, which have predetermined bidding power, and have
# them perform one bidding war. As of 6/7/20, this does not include the ability
# to modify bids after the initial bid has been made (as with a special power
# card or something)
def bidcombat(factions):
    waterbids = []
    secondbids = []

    for faction in factions:
        [waterbid, nutrientbid] = faction.bid(self.bidpower, self.strategy)
        waterbids.append(waterbid)
        nutrientbids.append(nutrientbid)

    # Copy the faction list
    waterfactions = factions
    nutrientfactions = factions

    zipped_water = zip(waterbids, waterfactions)
    zipped_nutrient = zip(nutrientbids, nutrientfactions)

    sorted_zip_water = sorted(zipped_water)
    sorted_zip_nutrient = sorted(zipped_nutrient)

    waterwinners = [element for _, element in sorted_zip_water]
    nutrientwinners = [element for _, element in sorted_zip_nutrient]

    print(waterwinners)
    print(' ')
    print(nutrientwinners)

    return [waterwinners, nutrientwinners]



# Maybe read in these values from a tab-delimited Excel sheet to make it easy to
# change
twoplayervals = np.array([[1, 0],
                        [2, 0],
                        [2, 1],
                        [3, 1],
                        [3, 2],
                        [4, 2],
                        [5, 2],
                        [5, 3],
                        [6, 3],
                        [7, 3],
                        [7, 4],
                        [8, 4],
                        [9, 4],
                        [9, 5],
                        [9, 6]
                        ])
# IT MIGHT BE WORTH HAVING SOMETHING TO INCENTIVIZE THE HIGH BIDDER TO CUT IT
# CLOSE, AND IT MIGHT BE WORTH HAVING THE STRATEGY CHANGE BASED ON THE BIDDING
# POWER OF THE OTHER PLAYERS
