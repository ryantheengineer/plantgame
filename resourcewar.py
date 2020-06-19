


def fillbag(nblue,nbrown):
    # Fill "bag" with resources that will be bid over
    bag = []
    for i in range(0, nblue):
        bag.append("Blue")

    for i in range(0, nbrown):
        bag.append("Brown")

    return bag
