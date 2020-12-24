import random
import numpy as np
import statistics as st
# import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fillbag(nblue,nbrown):
    # Fill "bag" with resources that will be bid over
    bag = []
    for i in range(0, nblue):
        bag.append("Blue")

    for i in range(0, nbrown):
        bag.append("Brown")

    return bag

def mixbag(bag):
    # Mix the bag in preparation for drawing
    random.shuffle(bag)
    return bag

def drawbag(nresources, bag):
    # Draw a certain number of resources from the shuffled bag
    if nresources < len(bag):
        drawn = bag[0:nresources]
        bag = bag[nresources:len(bag)]
    else:
        drawn = bag
        bag = []
    return(drawn, bag)

def rollfordraw(n1sides, n2sides):
    # Roll two dice of specified sides (usually these inputs would be 6, 6) to
    # determine how many resources to draw from the shuffled bag
    D1 = random.randint(1, n1sides)
    D2 = random.randint(1, n2sides)

    sum = D1 + D2
    return sum


# class Player:
#     def __init__(self, needblue, needbrown, bidpower, oppntbidpwr):
#         self.needblue = needblue
#         self.needbrown = needbrown
#         self.bidpower = bidpower
#         self.oppntbidpwr = oppntbidpwr
#         self.inbag = []
#         self.blueavail = []
#         self.brownavail = []
#
#     # Check how many total resources are available (left in the bag)
#     def seebag(self, bag):
#         self.inbag = len(bag)
#
#     def seeresdraw(self, blueavail, brownavail):
#         self.blueavail = blueavail
#         self.brownavail = brownavail
#
#
#
#     def calcbid(self, method):
#         if method == "allin":
#             # Bid everything on the first bid (bad idea but easy to test)
#             bid = self.bidpower
#
#         elif method == "proportional":
#             # Bid a proportional amount of player's bid power based on the
#             # proportion of the available resources to the total resources (bag
#             # + drawn resources)
#             resfrac = (self.blueavail + self.brownavail)/(self.inbag + self.blueavail + self.brownavail)
#             bid = resfrac*self.bidpower
#             if bid < 0:
#                 bid = 0
#             elif bid > self.bidpower:
#                 bid = self.bidpower
#             else:
#                 bid = int(round(bid))
#
#         # elif method == "outbid_proportional":
#             # Assume the opponents are bidding proportionally, and try to barely
#             # outbid them
#
#         elif method == "fillneeds":
#             # If the available resources will fill all the needs of the player,
#             # put everything on this bid. Otherwise, treat as a regular
#             # proportional bid
#             if self.blueavail >= self.needblue and self.brownavail >= self.needbrown:
#                 bid = self.bidpower
#             else:
#                 resfrac = (self.blueavail + self.brownavail)/(self.inbag + self.blueavail + self.brownavail)
#                 bid = resfrac*self.bidpower
#                 if bid < 0:
#                     bid = 0
#                 elif bid > self.bidpower:
#                     bid = self.bidpower
#                 else:
#                     bid = int(round(bid))
#
#         else:
#             # Randomly bid if the input string doesn't match a method string
#             print("Random bid enacted")
#             bid = random.randint(0,self.bidpower)
#
#
#
#         return bid
#
#     def reducebidpower(self, bid):
#         self.bidpower = self.bidpower - bid




# Testing code here before use with larger simulation and balancing
if __name__ == "__main__":
    print("running the main function")
    # Test the typical breakdown of the number of bidding rounds that occur with
    # dice of certain sizes and certain numbers of resources (maybe breaking it
    # down further to the number of each type). Get statistical results and plot
    # with histograms or box plots. This will be important for determining if
    # players with bid advantage will always be able to take available resources
    # or if there is an opportunity for the underdog. If the underdog
    # always loses, then maybe an adjustment to the bidding mechanic or a shift
    # to more of a war gaming mechanic might be necessary (i.e. dice rolls where
    # players get more dice for having more units in the contested spaces)

    ntests = 1000
    maxblue = 20
    maxbrown = 20
    n1sides = 6
    n2sides = 6
    results = np.zeros([maxblue, maxbrown, ntests]) # Results array, which will be filled with the number of resource groups that are available

    for i in range(0, maxblue):
        nblue = i + 1

        for j in range(0, maxbrown):
            nbrown = j + 1

            for k in range(0, ntests):
                statusmessage = "\n{} Blue, {} Brown, Test {}/{}".format(nblue, nbrown, k+1, ntests)
                print(statusmessage)
                drawcount = 0
                bag = fillbag(nblue,nbrown)
                bag = mixbag(bag)
                while len(bag) > 0:
                    drawcount += 1
                    # drawmsg = "Draw: {}".format(drawcount)
                    # print(drawmsg)
                    nresources = rollfordraw(n1sides, n2sides)
                    # nresourcesmsg = "\tnresources: {}".format(nresources)
                    # print(nresourcesmsg)
                    # bagmsg = "\tBag: {}".format(bag)
                    # print(bagmsg)
                    [drawn, bag] = drawbag(nresources, bag)
                    # drawnmsg = "\tDrawn: {}".format(drawn)
                    # print(drawnmsg)
                results[i, j, k] = drawcount

    averages = np.zeros([maxblue, maxbrown])
    stdevs = np.zeros([maxblue, maxbrown])
    for i in range(0, maxblue):
        for j in range(0, maxbrown):
            averages[i,j] = st.mean(results[i,j,:])
            stdevs[i,j] = st.stdev(results[i,j,:])

    averagesfile = "averages_{}x{}.csv".format(n1sides, n2sides)
    np.savetxt(averagesfile, averages, delimiter=',', fmt='%s')

    stdevsfile = "stdevs_{}x{}.csv".format(n1sides, n2sides)
    np.savetxt(stdevsfile, stdevs, delimiter=',', fmt='%s')


    # Make a 3D surface plot of the results
    hf = plt.figure()
    ha = hf.add_subplot(111, projection='3d')

    x = range(maxblue)
    y = range(maxbrown)

    X, Y = np.meshgrid(x, y)
    ha.plot_surface(X, Y, stdevs)

    plt.show()
