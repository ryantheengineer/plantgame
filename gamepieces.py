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
        
        
class MainBoard:    
    def __init__(self, n_region_spaces=None, resource_triggers=None, resource_values=None):
        # n_region_spaces: A list of 6 values, with values from 3 to 12
        if n_region_spaces == None:
            self.n_region_spaces = [random.randint(3,12) for i in range(0,6)]
        else:
            self.n_region_spaces = n_region_spaces
            
        # resource_triggers: 3x6 numpy array of values from 1 to 12
        if resource_triggers == None:
            resource_triggers = np.zeros([3,6])
            for i in range(0,3):
                for j in range(0,6):
                    resource_triggers[i,j] = random.randint(1,12)
        self.resource_triggers = resource_triggers
        
        # resource_values: 3x6 numpy array of values from 1 to 6
        if resource_values == None:
            resource_values = np.zeros([3,6])
            for i in range(0,3):
                for j in range(0,6):
                    resource_values[i,j] = random.randint(1,6)
        self.resource_values = resource_values
        
    def simulate_n_resource_rolls(self):
        # Simulate n resource rolls and gather statistics on amounts of resources gained
        
        

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
        
    mainboard = MainBoard()