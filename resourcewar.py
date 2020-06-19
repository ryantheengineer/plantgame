import random
import numpy as np

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
    drawn = bag[0:nresources]
    bag = bag[nresources:len(bag)]
    return(drawn, bag)


class Player:
    def __init__(self, needblue, needbrown, bidpower, oppntbidpwr):
        self.needblue = needblue
        self.needbrown = needbrown
        self.bidpower = bidpower
        self.oppntbidpwr = oppntbidpwr
        self.resavail = []
        self.blueavail = []
        self.brownavail = []

    # Check how many total resources are available (left in the bag)
    def seebag(self, bag):
        self.resavail = len(bag)

    def seeresdraw(self, blueavail, brownavail):
        self.blueavail = blueavail
        self.brownavail = brownavail

    def calcbid(self, method):
        if method == "random":
            bid = random.randint(0,self.bidpower)
        elif method == "proportional":
            resfrac = (self.blueavail + self.brownavail)

        return bid



# Testing code here before use with larger simulation and balancing
if __name__ == "__main__":
