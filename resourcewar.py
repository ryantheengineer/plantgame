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
        self.inbag = []
        self.blueavail = []
        self.brownavail = []

    # Check how many total resources are available (left in the bag)
    def seebag(self, bag):
        self.inbag = len(bag)

    def seeresdraw(self, blueavail, brownavail):
        self.blueavail = blueavail
        self.brownavail = brownavail



    def calcbid(self, method):
        if method == "allin":
            # Bid everything on the first bid (bad idea but easy to test)
            bid = self.bidpower

        elif method == "proportional":
            # Bid a proportional amount of player's bid power based on the
            # proportion of the available resources to the total resources (bag
            # + drawn resources)
            resfrac = (self.blueavail + self.brownavail)/(self.inbag + self.blueavail + self.brownavail)
            bid = resfrac*self.bidpower
            if bid < 0:
                bid = 0
            elif bid > self.bidpower:
                bid = self.bidpower
            else:
                bid = int(round(bid))

        elif method == "outbid_proportional":
            # Assume the opponents are bidding proportionally, and try to barely
            # outbid them

        elif method == "fillneeds":
            # If 

        else:
            # Randomly bid if the input string doesn't match a method string
            print("Random bid enacted")
            bid = random.randint(0,self.bidpower)



        return bid

    def reducebidpower(self, bid):
        self.bidpower = self.bidpower - bid




# Testing code here before use with larger simulation and balancing
if __name__ == "__main__":
