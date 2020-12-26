# Examine the effects of different die rolling combinations to determine what
# resource conversions to do for each region


import simulategame as sg
from matplotlib import pyplot as plt
# import pandas as pd
import numpy as np
import pprint

# NOTE: sort_resource_pool needs to be linked to a number of hexes that are involved
# in a combat so that the appropriate number of resources will be used. This means running
# a LOT of different scenarios and replotting box plot distributions for each number
# of hexes
def sort_resource_pool(resource):
    # Set the resource pool values and return an array of resource values
    resource_table = np.array([[3, 2, 0, 0, 0, 0],
                                [4, 3, 3, 0, 0, 0],
                                [6, 4, 3, 2, 0, 0],
                                [8, 6, 3, 2, 1, 0]])
    resource_pools = np.zeros([1, 6])

    if resource <= 5:
        maxpools = 2
        for i in range(0, maxpools):
            while (resource > 0) and (resource_pools[0,i] < resource_table[0,i]):
                resource -= 1
                resource_pools[0,i] += 1
    elif resource > 5 and resource <= 10:
        maxpools = 3
        for i in range(0, maxpools):
            while resource > 0 and resource_pools[0,i] < resource_table[1,i]:
                resource -= 1
                resource_pools[0,i] += 1
    elif resource > 10 and resource <= 15:
        maxpools = 4
        for i in range(0, maxpools):
            while resource > 0 and resource_pools[0,i] < resource_table[2,i]:
                resource -= 1
                resource_pools[0,i] += 1
    elif resource > 15 and resource <= 20:
        maxpools = 5
        for i in range(0, maxpools):
            while resource > 0 and resource_pools[0,i] < resource_table[3,i]:
                resource -= 1
                resource_pools[0,i] += 1
    else:
        extra_resource = resource - 20
        resource = 20
        maxpools = 5
        for i in range(0, maxpools):
            while resource > 0 and resource_pools[0,i] < resource_table[3,i]:
                resource -= 1
                resource_pools[0,i] += 1

        # If there are more than 20 of the current resource, then add the excess to the 1st pool
        resource_pools[0,0] += extra_resource

    return resource_pools





if __name__ == "__main__":

    # Simulate each possible combination of input dice (assuming 3 sided dice) and
    # output a histogram and statistics of the performance
    maxdice = 5
    nsims = 1000
    allhistograms = False
    ForestDice = (3, 2, 3)
    PlainsDice = (2, 2, 2)
    DesertDice = (1, 4, 2)


    allrollsarray = [[[0 for k in range(maxdice)] for j in range(maxdice)] for i in range(maxdice)]
    statsarray = [[[0 for k in range(maxdice)] for j in range(maxdice)] for i in range(maxdice)]

    # allrollsarray = np.empty([maxdice,maxdice,maxdice]) # Fill with raw rolls
    # statsarray = np.empty([maxdice,maxdice,maxdice]) # Fill with tuples of mean, median, standard deviation

    for waterdice in range(1,maxdice+1):
        for sundice in range(1,maxdice+1):
            for nutrientdice in range(1,maxdice+1):
                # Create new output array
                # rollarray = [[0 for j in range(3)] for i in range(nsims)]
                # print(len(rollarray)) # rows
                # print(len(rollarray[0])) # columns
                rollarray = np.empty([nsims,3])
                # pprint.pprint(rollarray)
                # wait = input("Press Enter to continue")
                resourcepools = np.empty([nsims,3,6]) # a row for each simulation, a column for each resource type, a page for each resource pool

                for i in range(0,nsims):
                    water, sun, nutrient = sg.rollforresources(waterdice, sundice, nutrientdice)
                    # print(water)
                    rollarray[i,0] = water
                    rollarray[i,1] = sun
                    rollarray[i,2] = nutrient

                    # Simulate the resource pool breakdown (using both ways of starting
                    # from the largest pool and starting from the smallest pool)
                    resourceroll = [water, sun, nutrient]

                    for j in range(0,3):
                        pools = sort_resource_pool(resourceroll[j])

                        for k in range(0,6):
                            resourcepools[i,j,k] = pools[0,k]



                # resourcepools will need to be plotted as a set of box plots, with groups of 3 box plots for each of the 6 resource pools
                # For ideas of how to do this, see: https://stackoverflow.com/questions/16592222/matplotlib-group-boxplots

                allrollsarray[waterdice-1][sundice-1][nutrientdice-1] = rollarray
                # pprint.pprint(rollarray)
                # print('')
                # pprint.pprint(rollarray[:,0])
                # print('')

                waterstats = (np.mean(rollarray[:,0]), np.median(rollarray[:,0]), np.std(rollarray[:,0]))
                sunstats = (np.mean(rollarray[:,1]), np.median(rollarray[:,1]), np.std(rollarray[:,1]))
                nutrientstats = (np.mean(rollarray[:,2]), np.median(rollarray[:,2]), np.std(rollarray[:,2]))

                statsarray[waterdice-1][sundice-1][nutrientdice-1] = (waterstats, sunstats, nutrientstats)

                if allhistograms is True:
                    bins = np.linspace(1,16,16)
                    plt.hist(rollarray[:,0], bins, alpha=0.5, label='Water')
                    plt.hist(rollarray[:,1], bins, alpha=0.5, label='Sun')
                    plt.hist(rollarray[:,2], bins, alpha=0.5, label='Nutrients')
                    plt.legend(loc='upper right')
                    titlestring = "{} Water dice, {} Sun dice, {} Nutrient dice".format(waterdice, sundice, nutrientdice)
                    plt.title(titlestring)
                    plt.show()
                else:
                    if waterdice == ForestDice[0] and sundice == ForestDice[1] and nutrientdice == ForestDice[2]:
                        bins = np.linspace(1,16,16)
                        plt.hist(rollarray[:,0], bins, alpha=0.5, label='Water')
                        plt.hist(rollarray[:,1], bins, alpha=0.5, label='Sun')
                        plt.hist(rollarray[:,2], bins, alpha=0.5, label='Nutrients')
                        plt.legend(loc='upper right')
                        titlestring = "{} Water dice, {} Sun dice, {} Nutrient dice".format(waterdice, sundice, nutrientdice)
                        plt.title(titlestring)
                        plt.suptitle("Forest")
                        plt.show()
                    elif waterdice == PlainsDice[0] and sundice == PlainsDice[1] and nutrientdice == PlainsDice[2]:
                        bins = np.linspace(1,16,16)
                        plt.hist(rollarray[:,0], bins, alpha=0.5, label='Water')
                        plt.hist(rollarray[:,1], bins, alpha=0.5, label='Sun')
                        plt.hist(rollarray[:,2], bins, alpha=0.5, label='Nutrients')
                        plt.legend(loc='upper right')
                        titlestring = "{} Water dice, {} Sun dice, {} Nutrient dice".format(waterdice, sundice, nutrientdice)
                        plt.title(titlestring)
                        plt.suptitle("Plains")
                        plt.show()
                    elif waterdice == DesertDice[0] and sundice == DesertDice[1] and nutrientdice == DesertDice[2]:
                        bins = np.linspace(1,16,16)
                        plt.hist(rollarray[:,0], bins, alpha=0.5, label='Water')
                        plt.hist(rollarray[:,1], bins, alpha=0.5, label='Sun')
                        plt.hist(rollarray[:,2], bins, alpha=0.5, label='Nutrients')
                        plt.legend(loc='upper right')
                        titlestring = "{} Water dice, {} Sun dice, {} Nutrient dice".format(waterdice, sundice, nutrientdice)
                        plt.title(titlestring)
                        plt.suptitle("Desert")
                        plt.show()
                # wait = input("Press Enter to continue")





    # For each individual simulation, run all the possible resource conversions and
    # carbon conversion possibilities and get distributions of carbon and plants out
