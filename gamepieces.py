import numpy as np
import random 
import pandas as pd

plant_sizes = ["Small", "Medium", "Large"]
regions = ["Rainforest", "Grassland", "Desert", "Deciduous Forest", "Evergreen Forest", "Tundra"]

class PlantCard:
    def __init__(self, name, plant_size=None, region_list=None, water=None,
                 sun=None, nutrient=None, carbon_out=None, carbon_in=None, plants_out=None):
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
            
        if carbon_out == None:
            self.carbon_out = random.randint(1,5)
        else:
            self.carbon_out = carbon_out
            
        if carbon_in == None:
            self.carbon_in = random.randint(1,5)
        else:
            self.carbon_in = carbon_in
            
        if plants_out == None:
            self.plants_out = random.randint(1,5)
        else:
            self.plants_out = plants_out
            
    def print_card(self):
        # Print card attributes for quick viewing in terminal
        print("Name:\t{}".format(self.name))
        print("Size:\t{}".format(self.plant_size))
        print("Regions:\t{}".format(self.region_list))
        print("Water:\t{}".format(self.water))
        print("Sun:\t{}".format(self.sun))
        print("Nutrient:\t{}".format(self.nutrient))
        print("Carbon:\t{}".format(self.carbon_out))
        
        
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
        
    def simulate_n_resource_rolls(self, n_rolls):
        # Simulate n resource rolls and gather statistics on amounts of resources gained
        pass
        

# PlayerBoard class holds resources and cards for a specific player, including
# water, sunlight, nutrients, carbon_out, plant cards, and other action cards
class PlayerBoard:
    def __init__(self, plantcards):
        pass

def discover_plant_desired_carbon(rolltrigger, turns_sim, turns_desired, carbon_desired, n_spaces_occupied, max_resource, max_require, max_carbon_gain):
    # Goal of this function is to find the minimum functioning level of plant
    # card characteristics for a given scenario: a given roll trigger value,
    # a desired number of turns to achieve the goal (get a certain amount of
    # carbon in the time desired), the number of spaces occupied.
    
    # Cycle through resources and adjust the plant card characteristics to
    # achieve the desired result
    
    # Initialize lists for creating a DataFrame later
    water_activated = []
    sun_activated = []
    nutrient_activated = []
    water_in = []
    sun_in = []
    nutrient_in = []
    carbon_out = []
    turns_to_goal = []
    
    n_sims = 100
    n_turns = turns_sim
    
    for j in range(1, max_resource+1):
        for k in range(1, max_resource+1):
            for m in range(1, max_resource+1):
                
                
                sims = np.zeros([n_turns,3,n_sims])
                for i in range(n_sims):
                    gained = np.zeros([n_turns,3])
                    for n in range(len(gained)):
                        # # 2D6
                        # d1 = random.randint(1,6)
                        # d2 = random.randint(1,6)
                        
                        # 2D3
                        d1 = random.randint(1,3)
                        d2 = random.randint(1,3)
                        dsum = d1 + d2
                        
                        if dsum == rolltrigger:
                            gained[n,0] = j * n_spaces_occupied
                            gained[n,1] = k * n_spaces_occupied
                            gained[n,2] = m * n_spaces_occupied
                            
                    gained_sum = np.zeros([n_turns,3])
                    for n in range(len(gained_sum)):
                        gained_sum[n,0] = np.sum(gained[:n,0])
                        gained_sum[n,1] = np.sum(gained[:n,1])
                        gained_sum[n,2] = np.sum(gained[:n,2])
                    
                    
                    sims[:,:,i] = gained_sum
                    
                    
                sim_means = np.zeros([n_turns,3])
                for turn in range(n_turns):
                    for resource in range(3):
                        sim_means[turn,resource] = np.mean(sims[turn,resource,:])
                        
                # print("\n{} spaces occupied:".format(n_spaces_occupied))
                # print("\n{} water, {} sun, {} nutrient gained on activation".format(j,k,m))
                # print("{} sun gained on activation".format(k))
                # print("{} nutrient gained on activation".format(m))
                # print(sim_means)
                
                # Iterate through plant card designs
                for w in range(1,max_require+1):
                    for x in range(1,max_require+1):
                        for y in range(1,max_require+1):
                            for z in range(1,max_carbon_gain+1):
                                plant_card = PlantCard("A",water=w,sun=x,nutrient=y,carbon_out=z)
                                
                                water_activated.append(j)
                                sun_activated.append(k)
                                nutrient_activated.append(m)
                                water_in.append(w)
                                sun_in.append(x)
                                nutrient_in.append(y)
                                carbon_out.append(z)
                                
                                
                                needs_satisfied = np.zeros([n_turns,3])
                                for turn in range(n_turns):
                                    needs_satisfied[turn,0] = sim_means[turn,0] // plant_card.water
                                    needs_satisfied[turn,1] = sim_means[turn,1] // plant_card.sun
                                    needs_satisfied[turn,2] = sim_means[turn,2] // plant_card.nutrient
                            
                                # plant_card.print_card()
                                # print(needs_satisfied)
                                
                                carbon_gained = np.zeros(n_turns)
                                # plants_gained = np.zeros(n_turns)
                                for turn in range(n_turns):
                                    carbon_gained[turn] = np.min(needs_satisfied[turn,:]) * plant_card.carbon_out
                                    # plants_gained[turn] = (carbon_gained[turn] // plant_card.carbon_in) * plant_card.plants_out
                                    
                                carbon_turns = 0
                                for gained in carbon_gained:
                                    if gained < carbon_desired:
                                        carbon_turns += 1
                                        
                                turns_to_goal.append(carbon_turns)
                                # print("Carbon gained each turn: {}".format(carbon_gained))
                                # print("Plants gained each turn: {}".format(plants_gained))
                                
    # Create dataframe from data
    data = {"Water Activated":water_activated, "Sun Activated":sun_activated,
            "Nutrient Activated":nutrient_activated, "Water In":water_in,
            "Sun In":sun_in, "Nutrient In":nutrient_in, "Carbon Out":carbon_out,
            "Turns to Goal":turns_to_goal}
    df = pd.DataFrame(data)
    
    # Suggest biomes that thematically fit with the resources that activate
    df_compatible, compatible_biomes = suggest_biomes(df, turns_desired, max_require)
    # biomes = []
    
    # biomes_list = ["Rainforest", "Grassland", "Desert", "Deciduous Forest", "Evergreen Forest", "Tundra"]
    # for i in range(len(df)):
    #     biomes_specific = []
    #     if df["Water Activated"].iloc[i] <= 2:
    #         biomes_specific.append("Desert")
    #         biomes_specific.append("Tundra")
    #     if df["Water Activated"].iloc[i] > 2 and df["Water Activated"].iloc[i] < 5:
    #         biomes_specific.append("Grassland")
    #         biomes_specific.append("Deciduous Forest")
    #         biomes_specific.append("Evergreen Forest")
    #     if df["Water Activated"].iloc[i] >= 5:
    #         biomes_specific.append("Rainforest")
    #     if df["Sun Activated"].iloc[i] <= 2:
    #         biomes_specific.append("Rainforest")
    #         biomes_specific.append("Tundra")
    #     if df["Sun Activated"].iloc[i] <= 3:
    #         biomes_specific.append("Evergreen Forest")
    #     if df["Sun Activated"].iloc[i] > 3:
    #         biomes_specific.append("Desert")
    #         biomes_specific.append("Grassland")
            
        
    #     biomes_specific = set(biomes_specific)
    #     biomes_specific = list(biomes_specific)
        
    #     biomes.append(biomes_specific)
        
    # df["Biomes"] = biomes
    
    # df_compatible = df[df["Turns to Goal"] == turns_desired]
    
    # compatible_biomes_dataframes = []
    # for biome in biomes_list:
    #     selection = [biome]
    #     df_compatible_biome = df_compatible[pd.DataFrame(df_compatible.Biomes.tolist()).isin(selection).any(1).values]
    #     compatible_biomes_dataframes.append(df_compatible_biome)
        
    # compatible_biomes = {"Rainforest":compatible_biomes_dataframes[0],
    #                      "Grassland":compatible_biomes_dataframes[1],
    #                      "Desert":compatible_biomes_dataframes[2],
    #                      "Deciduous Forest":compatible_biomes_dataframes[3],
    #                      "Evergreen Forest":compatible_biomes_dataframes[4],
    #                      "Tundra":compatible_biomes_dataframes[5]}
    
    return df, df_compatible, compatible_biomes


def suggest_biomes(df, turns_desired, max_require):
    # Suggest biomes that thematically fit with the resources that activate
    biomes = []
    biomes_list = ["Rainforest", "Grassland", "Desert", "Deciduous Forest", "Evergreen Forest", "Tundra"]
    
    # Set thresholds for thematic biome resource levels
    # Rainforest
    min_water_rainforest = int(np.around((3/5)*max_require))
    max_water_rainforest = max_require
    min_sun_rainforest = 1
    max_sun_rainforest = int(np.around((3/5)*max_require))
    min_nutrient_rainforest = int(np.around((3/5)*max_require))
    max_nutrient_rainforest = max_require
    
    # Grassland
    min_water_grassland = int(np.around((2/5)*max_require))
    max_water_grassland = int(np.around((4/5)*max_require))
    min_sun_grassland = int(np.around((3/5)*max_require))
    max_sun_grassland = max_require
    min_nutrient_grassland = int(np.around((1/5)*max_require))
    max_nutrient_grassland = max_require
    
    # Desert
    min_water_desert = 1
    max_water_desert = int(np.around((2/5)*max_require))
    min_sun_desert = int(np.around((4/5)*max_require))
    max_sun_desert = max_require
    min_nutrient_desert = 1
    max_nutrient_desert = int(np.around((3/5)*max_require))
    
    # Deciduous Forest
    min_water_deciduous = 1
    max_water_deciduous = int(np.around((4/5)*max_require))
    min_sun_deciduous = int(np.around((2/5)*max_require))
    max_sun_deciduous = max_require
    min_nutrient_deciduous = 1
    max_nutrient_deciduous = int(np.around((4/5)*max_require))
    
    # Evergreen Forest
    min_water_evergreen = 1
    max_water_evergreen = int(np.around((4/5)*max_require))
    min_sun_evergreen = 1
    max_sun_evergreen = int(np.around((4/5)*max_require))
    min_nutrient_evergreen = 1
    max_nutrient_evergreen = int(np.around((3/5)*max_require))
    
    # Tundra
    min_water_tundra = 1
    max_water_tundra = int(np.around((2/5)*max_require))
    min_sun_tundra = 1
    max_sun_tundra = int(np.around((2/5)*max_require))
    min_nutrient_tundra = 1
    max_nutrient_tundra = int(np.around((2/5)*max_require))
    
    for i in range(len(df)):
        biomes_specific = []
        water = df["Water Activated"].iloc[i]
        sun = df["Sun Activated"].iloc[i]
        nutrient = df["Nutrient Activated"].iloc[i]
        
        # Rainforest
        if water >= min_water_rainforest and water <= max_water_rainforest:
            if sun >= min_sun_rainforest and sun <= max_sun_rainforest:
                if nutrient >= min_nutrient_rainforest and nutrient <= max_nutrient_rainforest:
                    biomes_specific.append("Rainforest")
                    
        # Grassland
        if water >= min_water_grassland and water <= max_water_grassland:
            if sun >= min_sun_grassland and sun <= max_sun_grassland:
                if nutrient >= min_nutrient_grassland and nutrient <= max_nutrient_grassland:
                    biomes_specific.append("Grassland")
                    
        # Desert
        if water >= min_water_desert and water <= max_water_desert:
            if sun >= min_sun_desert and sun <= max_sun_desert:
                if nutrient >= min_nutrient_desert and nutrient <= max_nutrient_desert:
                    biomes_specific.append("Desert")
                    
        # Deciduous Forest
        if water >= min_water_deciduous and water <= max_water_deciduous:
            if sun >= min_sun_deciduous and sun <= max_sun_deciduous:
                if nutrient >= min_nutrient_deciduous and nutrient <= max_nutrient_deciduous:
                    biomes_specific.append("Deciduous Forest")
                    
        # Evergreen Forest
        if water >= min_water_evergreen and water <= max_water_evergreen:
            if sun >= min_sun_evergreen and sun <= max_sun_evergreen:
                if nutrient >= min_nutrient_evergreen and nutrient <= max_nutrient_evergreen:
                    biomes_specific.append("Evergreen Forest")
                    
        # Tundra
        if water >= min_water_tundra and water <= max_water_tundra:
            if sun >= min_sun_tundra and sun <= max_sun_tundra:
                if nutrient >= min_nutrient_tundra and nutrient <= max_nutrient_tundra:
                    biomes_specific.append("Tundra")
            
        
        biomes_specific = set(biomes_specific)
        biomes_specific = list(biomes_specific)
        
        biomes.append(biomes_specific)
        
    df["Biomes"] = biomes
    
    df_compatible = df[df["Turns to Goal"] == turns_desired]
    
    compatible_biomes_dataframes = []
    for biome in biomes_list:
        selection = [biome]
        df_compatible_biome = df_compatible[pd.DataFrame(df_compatible.Biomes.tolist()).isin(selection).any(1).values]
        compatible_biomes_dataframes.append(df_compatible_biome)
        
    compatible_biomes = {"Rainforest":compatible_biomes_dataframes[0],
                         "Grassland":compatible_biomes_dataframes[1],
                         "Desert":compatible_biomes_dataframes[2],
                         "Deciduous Forest":compatible_biomes_dataframes[3],
                         "Evergreen Forest":compatible_biomes_dataframes[4],
                         "Tundra":compatible_biomes_dataframes[5]}
    
    return df_compatible, compatible_biomes


if __name__ == "__main__":
    rolltrigger = 3 # sum of 2D3
    turns_sim = 10
    turns_desired = 2
    if turns_desired > turns_sim:
        raise ValueError("turns_desired should be <= to turns_sim for useful results")
    carbon_desired = 3
    n_spaces_occupied = 2
    max_resource = 5
    max_require = 5
    max_carbon_gain = 3
    
    df_all, df_compatible, compatible_biomes = discover_plant_desired_carbon(rolltrigger, turns_sim, turns_desired, carbon_desired, n_spaces_occupied, max_resource, max_require, max_carbon_gain)
    
    # Summarize data
    n_all = len(df_all)
    n_compatible = len(df_compatible)
    pct_compatible = 100 * (n_compatible/n_all)
    
    if pct_compatible == 0.0:
        print("No compatible card designs were found for the chosen inputs.")
    else:
        print("{}% compatible scenarios".format(pct_compatible))
        
        n_rainforest_designs = len(compatible_biomes["Rainforest"])
        n_grassland_designs = len(compatible_biomes["Grassland"])
        n_desert_designs = len(compatible_biomes["Desert"])
        n_deciduous_designs = len(compatible_biomes["Deciduous Forest"])
        n_evergreen_designs = len(compatible_biomes["Evergreen Forest"])
        n_tundra_designs = len(compatible_biomes["Tundra"])
        
        print("\nScenario Description:")
        print("Roll trigger:\t{} (2D3)".format(rolltrigger))
        print("Spaces occupied:\t{}".format(n_spaces_occupied))
        print("Carbon goal:\t{}".format(carbon_desired))
        print("Desired turns:\t{}".format(turns_desired))
        
        
        print("\nCompatible Scenarios:")
        print("Total:\t{}".format(n_compatible))
        print("Rainforest:\t{}".format(n_rainforest_designs))
        print("Grassland:\t{}".format(n_grassland_designs))
        print("Desert:\t{}".format(n_desert_designs))
        print("Deciduous Forest:\t{}".format(n_deciduous_designs))
        print("Evergreen Forest:\t{}".format(n_evergreen_designs))
        print("Tundra:\t{}".format(n_tundra_designs))
    
    
    # plant_names = ["A"]
    # plant_cards = [PlantCard(name,plant_size=None, region_list=None, water=3,
    #              sun=2, nutrient=1, carbon_out=3, carbon_in=1, plants_out=3) for name in plant_names]
    # for plant_card in plant_cards:
    #     plant_card.print_card()
    
    # # wait = input("\nPress Enter to continue")
    
    # trigger_val = 7
    
    # n_turns = 10
    
    # n_spaces_occupied = 5
    
    # n_sims = 500
        
    
    # for j in range(1,6):    # Number of water gained by activation
    #     for k in range(1,6):    # Number of sun gained by activation
    #         for m in range(1,6):    # Number of nutrient gained by activation
    #             sims = np.zeros([n_turns,3,n_sims])
    #             for i in range(n_sims):
    #                 gained = np.zeros([n_turns,3])
    #                 for n in range(len(gained)):
    #                     d1 = random.randint(1,6)
    #                     d2 = random.randint(1,6)
    #                     dsum = d1 + d2
                        
    #                     if dsum == trigger_val:
    #                         gained[n,0] = j * n_spaces_occupied
    #                         gained[n,1] = k * n_spaces_occupied
    #                         gained[n,2] = m * n_spaces_occupied
                            
    #                 gained_sum = np.zeros([n_turns,3])
    #                 for n in range(len(gained_sum)):
    #                     gained_sum[n,0] = np.sum(gained[:n,0])
    #                     gained_sum[n,1] = np.sum(gained[:n,1])
    #                     gained_sum[n,2] = np.sum(gained[:n,2])
                    
                    
    #                 sims[:,:,i] = gained_sum
                    
                    
    #             sim_means = np.zeros([n_turns,3])
    #             for turn in range(n_turns):
    #                 for resource in range(3):
    #                     sim_means[turn,resource] = np.mean(sims[turn,resource,:])
                        
    #             # print("\n{} spaces occupied:".format(n_spaces_occupied))
    #             print("\n{} water, {} sun, {} nutrient gained on activation".format(j,k,m))
    #             # print("{} sun gained on activation".format(k))
    #             # print("{} nutrient gained on activation".format(m))
    #             # print(sim_means)
                
    #             for i,plant_card in enumerate(plant_cards):
    #                 needs_satisfied = np.zeros([n_turns,3])
    #                 for turn in range(n_turns):
    #                     needs_satisfied[turn,0] = sim_means[turn,0] // plant_card.water
    #                     needs_satisfied[turn,1] = sim_means[turn,0] // plant_card.sun
    #                     needs_satisfied[turn,2] = sim_means[turn,0] // plant_card.nutrient
                
    #                 # plant_card.print_card()
    #                 # print(needs_satisfied)
                    
    #                 carbon_gained = np.zeros(n_turns)
    #                 plants_gained = np.zeros(n_turns)
    #                 for turn in range(n_turns):
    #                     carbon_gained[turn] = np.min(needs_satisfied[turn,:]) * plant_card.carbon_out
    #                     plants_gained[turn] = (carbon_gained[turn] // plant_card.carbon_in) * plant_card.plants_out
    #                 print("Carbon gained each turn: {}".format(carbon_gained))
    #                 print("Plants gained each turn: {}".format(plants_gained))
                        
    # plant_card.print_card()
                