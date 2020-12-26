import numpy as np
import pandas as pd
import resourcewar as rwr
import random


def initialize_cards():
    df = pd.read_csv("cards.csv", sep=",")

    sugarmaple = crd.Card(df, "Sugar maple")

    return sugarmaple

# class Game:
#     # Class made up of players, board, cards, resources, etc.
#
#
#
# class Player:
#     # Class to hold an individual player's cards and available resources
#

class PlantCard:
    def __init__(self, size, forest, plains, desert, water_in, sun_in,
        nutrient_in, carbon_out, carbon_in, plants_out, seedtype, bonustext):
        # Initialize the card with properties
        self.size = size
        self.forest = forest
        self.plains = plains
        self.desert = desert
        self.water_in = water_in
        self.sun_in = sun_in
        self.nutrient_in = nutrient_in
        self.carbon_in = carbon_in
        self.carbon_out = carbon_out
        self.plants_out = plants_out
        self.seedtype = seedtype
        self.bonustext = bonustext


class AvailableResources:
    def __init__(self, forest_resources, plains_resources, desert_resources):
        self.forest_resources = forest_resources # list of integers (i.e. [3, 6, 4])
        self.plains_resources = plains_resources
        self.desert_resources = desert_resources

class Player:
    def __init__(self, player, hand, discard, tableau, availableresources,
        carbon, smallcount, medcount, largecount):
        self.player = player
        self.hand = hand # This should automatically be the initial hand available to everyone
        self.discard = discard
        self.tableau = tableau
        self.availableresources = availableresources
        self.carbon = carbon
        self.smallcount = smallcount
        self.medcount = medcount
        self.largecount = largecount


# class Board:
#     def __init__(self):
#         # Create hex grid system with size limits, define regions, bonus spaces, piece counts per hex
#


def rollforresources(waterdice, sundice, nutrientdice):
    # input the number of dice to roll for each resource
    nsides = 3

    for i in range(0, 3):
        die = 0
        sum = 0

        if i == 0:
            dicecount = waterdice
        elif i == 1:
            dicecount = sundice
        elif i == 2:
            dicecount = nutrientdice
        else:
            print("ERROR WITH DICE COUNTS")

        while die < dicecount:
            roll = random.randint(1, nsides)
            # print(roll)
            sum += roll
            die += 1

        if i == 0:
            water = sum
        elif i == 1:
            sun = sum
        elif i == 2:
            nutrient = sum
        else:
            print("ERROR WITH DICE COUNTS")

    return water, sun, nutrient




if __name__ == "__main__":
    print("\nRunning the main function\n")
