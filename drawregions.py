from random import shuffle

# # Experiment with automating the full region list
# nRF = 3
# nAP = 2
# nDS = 2
# nCS = 3

regions = ["Rainforest", "Rainforest", "Rainforest", "Alpine", "Alpine",
    "Desert", "Desert", "Coast", "Coast", "Coast"]

allregions = "\nAll possible regions: {}".format(regions)
print(allregions)

# Shuffle the region tiles
shuffle(regions)

shuffledregions = "\nShuffled regions: {}".format(regions)
print(shuffledregions)

round1 = regions[0:5]
round2 = regions[5:10]

round1draw = "\nRound 1 regions: {}".format(round1)
round2draw = "\nRound 2 regions: {}".format(round2)

print(round1draw)
print(round2draw)
