# -*- coding: utf-8 -*-

import gridlab_lib as glm_lib
import random

list_def_appliances = [
    ["dishwasher", "1500", "1.5", "null", "3600"],
    ["washcloth", "500", "0.5", "null", "3600"],
    ["water_bomb", "850", "0.85", "null", "3600"],
    ["boiler", "1500", "1.5", "null", "3600"],
    ["dryer", "1000", "1.0", "null", "3600"],
    ["air_conditioning", "2000", "2.0", "null", "3600"],
    ["bomba_de_aquario", "5", "3.6", "null", "3600"],
    ["secadora_de_roupa", "1000", "8", "null", "3600"],
    ["dishwasher", "1500", "1.5", "null", "3600"],
    ["washcloth", "500", "0.5", "null", "3600"],
    ["water_bomb", "850", "0.85", "null", "3600"],
    ["boiler", "1500", "1.5", "null", "3600"],
    ["dryer", "1000", "1.0", "null", "3600"],
    ["air_conditioning", "2000", "2.0", "null", "3600"],
    ["bomba_de_aquario", "5", "3.6", "null", "3600"],
    ["secadora_de_roupa", "1000", "8", "null", "3600"],
    ["boiler", "1500", "1.5", "null", "3600"],
    ["dryer", "1000", "1.0", "null", "3600"],
    ["air_conditioning", "2000", "2.0", "null", "3600"],
    ["bomba_de_aquario", "5", "3.6", "null", "3600"],
    ["secadora_de_roupa", "1000", "8", "null", "3600"]
]

#list_def_appliances = [
#     ["dishwasher", "1000", "1", "null", "3600"],
#     ["washcloth", "1000", "1", "null", "3600"],
#     ["water_bomb", "1000", "1", "null", "3600"],
#     ["boiler", "1000", "1", "null", "3600"],
#     ["dryer", "1000", "1", "null", "3600"],
#     ["air_conditioning", "1000", "1", "null", "3600"],
#     ["dishwasher", "1000", "1", "null", "3600"],
#     ["washcloth", "1000", "1", "null", "3600"],
#     ["water_bomb", "1000", "1", "null", "3600"],
#     ["boiler", "1000", "1", "null", "3600"],
#     ["dryer", "1000", "1", "null", "3600"],
#     ["air_conditioning", "1000", "1", "null", "3600"]
#]



class Workload:

    def __init__(self, number_houses, number_household_appliances):
        self.list_houses = []
        self.number_houses = number_houses
        self.number_household_appliances = number_household_appliances
        self.create_all_houses(self.number_houses, self.number_household_appliances)

    def get_list_random_appliances(self, house_name, number_household_appliances):
        list_random_appliances = []
        for i in range(number_household_appliances):
            info = list_def_appliances[random.randint(0, number_household_appliances - 1)]
            appliance = glm_lib.Lights(house_name + info[0], info[1], info[2], info[3], info[4])
            list_random_appliances.append(appliance)
        return list_random_appliances

    def add_house(self, number_household_appliances):
        house = glm_lib.House("3600")
        house.add_list_appliance(self.get_list_random_appliances(house.name_of_house, number_household_appliances))
        return house

    def create_all_houses(self, number_of_houses, number_household_appliances):
        for i in range(number_of_houses):
            self.list_houses.append(self.add_house(number_household_appliances))

    def get_workload(self):
        return self.list_houses
