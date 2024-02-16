# -*- coding: utf-8 -*-

import random
import gridlab_lib as glm_lib


class Build_Schedule:
    def __init__(self, list_houses):
        self.list_houses = list_houses

    def get_list_houses(self):
        return self.list_houses

    def generate_random_schedule(self, appliance_id, number_of_hours, appliance_power):
        list_schedule = []
        for i in range(number_of_hours):
            list_schedule.append([appliance_id, random.randint(0, 23), appliance_power])
        return list_schedule

    def generate_list_random_schedule(self, list_os_appliances):
        list_random_schedule = []
        count = 0  # id_schedule
        for i in list_os_appliances:
            list_random_schedule.append(self.generate_random_schedule(count, random.randint(1, 4), i.power))
            count += 1
        return list_random_schedule

    def get_list_random_schedule_houses(self):
        list_random_schedule_houses = []
        for house in self.list_houses:
            list_random_schedule_houses.append(self.generate_list_random_schedule(house.get_list_appliances()))
        return list_random_schedule_houses

    def extract_hour_schedule_list(self, list_schedule):
        hour_schedules_list = []
        for schedules in list_schedule:
            temp_list = []
            for s in schedules:
                var = s[1]
                temp_list.append(s[1])
            hour_schedules_list.append(temp_list)
        # print("XXXXXXXXX")
        # print(hour_schedules_list)
        return self.remove_all_hour_duplicates(hour_schedules_list)

    def remove_all_hour_duplicates(self, hour_schedules_list):
        for i in hour_schedules_list:
            self.remove_hour_duplicates(i)
        return hour_schedules_list

    def remove_hour_duplicates(self, hour_schedules):
        for i in range(len(hour_schedules)):
            for j in range(len(hour_schedules)):
                if i != j and hour_schedules[i] == hour_schedules[j]:
                    hour_schedules[i] = self.generate_new_number(hour_schedules[i])

    def generate_new_number(self, number):
        new_number = random.randint(0, 23)
        while number == new_number:
            new_number = random.randint(0, 23)
        return new_number

    def extract_house_schedules(self, hour_schedules_list, house):
        list_obj_schedule = []
        temp_house_appliances_list = house.get_list_appliances()
        for i in range(len(hour_schedules_list)):
            name_schedule = house.name_of_house + "_schedule" + str(i)
            temp_house_appliances_list[i].set_schedule(name_schedule)
            list_obj_schedule.append(glm_lib.Schedule(name_schedule, hour_schedules_list[i]))
        return list_obj_schedule

    def update_house_schedule_list(self, all_schedule_list, house_of_lists):
        hour_schedules_list = []
        list_obj_schedule = []
        for i in range(len(house_of_lists)):
            temp_hour_schedules_list = self.extract_hour_schedule_list(all_schedule_list[i])
            temp_list_obj_schedule = self.extract_house_schedules(temp_hour_schedules_list, house_of_lists[i])
            hour_schedules_list.append(temp_hour_schedules_list)
            list_obj_schedule.append(temp_list_obj_schedule)
        return list_obj_schedule

    # def update_house_collections_schedule_list(self, collections_schedule, ):
