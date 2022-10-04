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

def discover_plant_desired_carbon(rolltrigger, turns_sim, turns_desired, carbon_desired, n_spaces_occupied, max_resource, max_require):
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
                        d1 = random.randint(1,6)
                        d2 = random.randint(1,6)
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
                            for z in range(1,max_require+1):
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
    
    df_compatible = df[df["Turns to Goal"] <= turns_desired]
    
    return df, df_compatible


if __name__ == "__main__":
    rolltrigger = 1
    turns_sim = 10
    turns_desired = 5
    carbon_desired = 3
    n_spaces_occupied = 1
    max_resource = 5
    max_require = 5    
    
    df_all, df_compatible = discover_plant_desired_carbon(rolltrigger, turns_sim, turns_desired, carbon_desired, n_spaces_occupied, max_resource, max_require)
    
    n_all = len(df_all)
    n_compatible = len(df_compatible)
    pct_compatible = 100 * (n_compatible/n_all)
    
    if pct_compatible == 0.0:
        print("No compatible card designs were found for the chosen inputs.")
    else:
        min_turns = min(df_compatible["Turns to Goal"])
        
        df_fastest = df_compatible[df_compatible["Turns to Goal"] == min_turns]
        
        n_fastest = len(df_fastest)
        pct_fastest = 100 * (n_fastest/n_all)
    
    
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
                