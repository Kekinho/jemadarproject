# -*- coding: utf-8 -*-

from datetime import date, timedelta
import random


class Recorder:
    def __init__(self, file_name, interval):
        self.file_name = file_name
        self.interval = interval

    def __str__(self):
        string = "object recorder{ \n"
        string += "property energy; \n"
        string += "file \"" + self.file_name + ".csv\"; \n"
        string += "interval " + self.interval + "; \n"
        string += "};\n\n"
        return string

    def __repr__(self):
        return self.__str__()


class PanelRecorder:
    def __init__(self, file_name, interval):
        self.file_name = file_name
        self.interval = interval

    def __str__(self):
        string = "object recorder{ \n"
        string += "property panel.energy; \n"
        string += "file \"" + self.file_name + ".csv\"; \n"
        string += "interval " + self.interval + "; \n"
        string += "};\n\n"
        return string

    def __repr__(self):
        return self.__str__()



class Lights:
    id = 0

    def __init__(self, name, installed_power, power, schedule, interval):
        self.__class__.id += 1
        self.name = name + str(self.__class__.id)
        self.installed_power = installed_power
        self.power = power
        self.schedule = schedule
        self.recorder = Recorder(self.name + "rec", interval)

    def get_name(self):
        return self.name

    def get_installed_power(self):
        return self.installed_power

    def get_power(self):
        return self.get_power()

    def get_schedule(self):
        return self.get_schedule()

    def set_schedule(self, schedule):
        self.schedule = schedule

    def __str__(self):
        string = "object lights {\n"
        string += "type HID; \n"
        string += "name " + self.name + ";\n"
        string += "installed_power " + self.installed_power + " W; \n"
        string += "shape \"type: analog; schedule: " + str(self.schedule) + "; power: " + self.power + " kW\"; \n"
        string += "\n"
        string += self.recorder.__str__()
        string += "};\n\n"
        return string

    def __repr__(self):
        return self.__str__()


class House:
    id = 0

    def __init__(self, interval):
        self.__class__.id += 1
        self.name_of_house = "house" + str(self.__class__.id)
        self.interval = interval
        self.list_appliances = []
        self.recorder = PanelRecorder(self.name_of_house + "output", self.interval)

    def add_appliances(self, name_appliance, installed_power, power, schedule_name):
        appliance = Lights(self.name_of_house + name_appliance, installed_power, power, schedule_name, self.interval)
        self.list_appliances.append(appliance)

    def get_name(self):
        return self.name_of_house

    def add_list_appliance(self, list_appliance):
        for appliance in list_appliance:
            self.list_appliances.append(appliance)

    def get_list_appliances(self):
        return self.list_appliances

    def name_appliances(self):
        list_name_appliances = []
        for i in self.list_appliances:
            list_name_appliances.append(self.list_appliances[i])
        return list_name_appliances

    def __str__(self):
        string = "object house { \n\n"
        string += "name " + self.name_of_house + "; \n"
        string += "parent Meter; \n"
        string += "floor_area 1250 sf; \n"
        string += "panel.power_factor 0.98; \n"
        string += "\n"
        for i in range(len(self.list_appliances)):
            string += str(self.list_appliances[i].__repr__())
        string += "\n"
        string += self.recorder.__str__()
        string += "\n"
        string += "};\n\n"
        return string

    def __repr__(self):
        return self.__str__()


class Clock:

    def __init__(self, days):
        self.days = days

    def __str__(self):
        string = "clock {\n"
        string += "timezone PST+8PDT;\n"
        string += "starttime '" + str(date.today()) + " 00:00:00 PDT';\n"
        string += "stoptime '" + str(
            date.today() + timedelta(days=self.days)) + " 01:00:00 PDT';\n"  # Uma hora a mais pra pegar o consumo total
        string += "} \n\n"
        return string

    def __repr__(self):
        return self.__str__()


class Schedule:

    def __init__(self, name, hour):
        self.name = name
        self.hour = hour

    def name(self):
        return self.name()

    def remove_hour_duplicates(self, hour_schedules):
        for i in range(len(hour_schedules)):
            for j in range(len(hour_schedules)):
                if i != j and hour_schedules[i] == hour_schedules[j]:
                    hour_schedules[i] = self.generate_new_number(hour_schedules[i])
        return hour_schedules

    def generate_new_number(self, number):
        new_number = random.randint(0, 23)
        while number == new_number:
            new_number = random.randint(0, 23)
        return new_number

    def __str__(self):
        string = "schedule " + self.name + " { \n"
        if type(self.hour) is list:
            self.remove_hour_duplicates(self.hour)
            for i in range(len(self.hour)):
                string += "* " + str(self.hour[i]) + " * * * 1.0 \n"
        else:
            string += "* " + str(self.hour) + " * * * 1.0 \n"
        string += "} \n\n"
        return string

    def __repr__(self):
        return self.__str__()


class Microgrid:

    def __init__(self):
        self.list_houses = []
        self.list_schedule = []

    def add_houses(self, house):
        self.list_houses.append(house)

    def add_list_houses(self, list_houses):
        for house in list_houses:
            self.list_houses.append(house)

    def get_list_houses(self):
        return self.list_houses

    def add_schedules(self, schedule):
        self.list_schedule.append(schedule)

    def add_list_schedules(self, list_schedule):
        for schedule in list_schedule:
            self.list_schedule.append(schedule)

    def clear_list_schedule(self):
        self.list_schedule.clear()

    def get_list_schedule(self):
        return self.list_schedule

    def get_to_string_houses(self):
        string = ""
        for i in range(len(self.list_houses)):
            string += self.list_houses[i].__repr__()
        return string

    def get_to_string_schedules(self):
        string = ""
        for i in range(len(self.list_schedule)):
            string += self.list_schedule[i].__repr__()
        return string

    def clean_string(self, string):
        string_temp = string
        deny_characters = "[,]"
        for i in range(0, len(deny_characters)):
            string_temp = string_temp.replace(deny_characters[i], "")
        return string_temp

    def __str__(self):
        return self.clean_string(self.get_to_string_schedules() + self.get_to_string_houses())

    def __repr__(self):
        return self.__str__()


def create_modules():
    string = "module powerflow;\n"
    string += "module assert;\n"
    string += "module tape;\n"
    string += "module climate;\n"
    string += "module residential { \n"
    string += "\t" + "implicit_enduses \n"
    string += "\t" + "LIGHTS|PLUGS|MICROWAVE|FREEZER|REFRIGERATOR|RANGE|WATERHEATER|CLOTHESWASHER|DRYER; \n"
    string += "} \n\n"
    # gridlab_input_file.write(string)
    return string


def create_object_climate(tmyfile):
    string = "object climate {\n"
    string += "tmyfile \"" + tmyfile + "\";"
    string += "\n} \n"
    return string


def create_object_triplex_meter():
    string = "object triplex_meter {\n"
    string += "name Meter; \n"
    string += "nominal_voltage 120.0; \n"
    string += "phases AS; \n"
    string += "} \n"
    return string
