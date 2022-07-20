import numpy as np
import random 

plant_sizes = ["Small", "Medium", "Large"]
regions = ["Rainforest", "Grassland", "Desert", "Deciduous Forest", "Evergreen Forest", "Tundra"]

class PlantCard:
    def __init__(self, name, plant_size=None, region_list=None, water=None,
                 sun=None, nutrient=None, carbon=None):
        # If parameters are not supplied, randomly choose or generate values for
        # the card, except for name
        self.name = name
        
        if plant_size == None:
            self.plant_size = random.choice(plant_sizes)
        else:
            self.plant_size = plant_size
        
        if region_list == None:
            n_regions = random.randint(1,3)
            self.region_list = random.sample(regions, n_regions)
        else:
            self.region_list = region_list
            
        if water == None:
            self.water = random.randint(1,5)
        else:
            self.water = water
            
        if sun == None:
            self.sun = random.randint(1,5)
        else:
            self.sun = sun
            
        if nutrient == None:
            self.nutrient = random.randint(1,5)
        else:
            self.nutrient = nutrient
            
        if carbon == None:
            self.carbon = random.randint(1,5)
        else:
            self.carbon = carbon
            
    def print_card(self):
        # Print card attributes for quick viewing in terminal
        print("\nName:\t{}".format(self.name))
        print("Size:\t{}".format(self.plant_size))
        print("Regions:\t{}".format(self.region_list))
        print("Water:\t{}".format(self.water))
        print("Sun:\t{}".format(self.sun))
        print("Nutrient:\t{}".format(self.nutrient))
        print("Carbon:\t{}".format(self.carbon))
        
        


# PlayerBoard class holds resources and cards for a specific player, including
# water, sunlight, nutrients, carbon, plant cards, and other action cards
class PlayerBoard:
    def __init__(self, plantcards):
        pass


if __name__ == "__main__":
    plant_names = ["A", "B", "C"]
    plant_cards = [PlantCard(name) for name in plant_names]
    for plant_card in plant_cards:
        plant_card.print_card()