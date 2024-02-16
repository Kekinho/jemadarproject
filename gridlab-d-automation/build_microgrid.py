# -*- coding: utf-8 -*-

import gridlab_lib as glm_lib


def create_static_schedule():
    list_schedule = []
    list_schedule.append(glm_lib.Schedule("schedule01", "18-23"))
    list_schedule.append(glm_lib.Schedule("schedule02", "12-14"))
    list_schedule.append(glm_lib.Schedule("schedule03", "06-17"))
    list_schedule.append(glm_lib.Schedule("schedule04", "00-23"))
    list_schedule.append(glm_lib.Schedule("schedule05", "01-10"))
    list_schedule.append(glm_lib.Schedule("schedule06", "18-20"))
    return list_schedule


def create_static_appliances(house_name):
    list_schedule = create_static_schedule()
    list_home_appliances = []
    list_home_appliances.append(glm_lib.Lights(house_name + "luz1", "110", "0.11", list_schedule[0], "3600"))
    list_home_appliances.append(glm_lib.Lights(house_name + "microwave1", "1200", "1.2", list_schedule[1], "3600"))
    list_home_appliances.append(glm_lib.Lights(house_name + "freezer1", "760", "0.1", list_schedule[2], "3600"))
    return list_home_appliances


def create_static_houses():
    list_house = []
    house01 = glm_lib.House("3600")
    house02 = glm_lib.House("3600")
    house03 = glm_lib.House("3600")
    house01.add_list_appliance(create_static_appliances(house01.name_of_house))
    house02.add_list_appliance(create_static_appliances(house02.name_of_house))
    house03.add_list_appliance(create_static_appliances(house03.name_of_house))
    list_house.append(house01)
    list_house.append(house02)
    list_house.append(house03)
    return list_house


def create_houses(number_of_houses, interval):
    list_house = []
    for i in range(number_of_houses):
        house_temp = glm_lib.House(interval)
        house_temp.add_list_appliance(create_static_appliances(house_temp.name_of_house))
        list_house.append(house_temp)
    return list_house


def create_static_microgrid(number_of_houses):
    microgrid = glm_lib.Microgrid()
    microgrid.add_list_schedules(create_static_schedule())
    microgrid.add_list_houses(create_houses(number_of_houses, "3600"))
    return microgrid


def create_microgrid(list_schedules, list_houses, interval_t):
    microgrid = glm_lib.Microgrid()
    microgrid.add_list_schedules(list_schedules)
    microgrid.add_list_houses(create_houses(list_houses, interval_t))
    return microgrid

