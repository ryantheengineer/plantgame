import numpy as np
import pandas as pd


class Card:
    def __init__(self, df, cardname):
        # df is a pandas dataframe read in of cards.csv
        # cardname is the string name of the card, not the variable name

        # Using the cardname indicator, get the card characteristics from cards.csv
        # df = pd.read_csv("cards.csv", sep=",")
        card_index = df[df["Name"] == cardname].index.to_numpy()
        card_index = int(card_index)
        cardstats = df.loc[card_index]

        self.name = cardstats.Name # string name
        self.size = cardstats.Size
        self.bidpower = cardstats.Bidpower
        self.maintain_cost = cardstats.Maintain_cost
        self.maintain_per = cardstats.Maintain_per
        self.mature = cardstats.Mature
        self.seedtype = cardstats.Seedtype
        self.sunlight_in = cardstats.Sunlight_in
        self.water_in = cardstats.Water_in
        self.nutrients_in = cardstats.Nutrients_in
        self.unique_resources = cardstats.Unique_resources
        self.wild_resources = cardstats.Wild_resources
        self.carbon_out = cardstats.Carbon_out
        self.alpine = cardstats.Alpine
        self.coast = cardstats.Coast
        self.desert = cardstats.Desert
        self.tropics = cardstats.Tropics
