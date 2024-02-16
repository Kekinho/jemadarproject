# -*- coding: utf-8 -*-
from decimal import Decimal
import build_gridlab_file as glm_build
import os
import csv
from pathlib import Path


def extract_consumption_from_gridlab_file(path_and_name_file):
    all_consumption = open(path_and_name_file)
    list_current_consumption = []
    list_time = []
    previus_consumption = 0
    for line in all_consumption:
        if line[0] != "#":
            temp01 = line.split(",")[0]
            temp02 = line.split(",")[1]
            time_hour = temp01[0:19]
            consumption = temp02[1:temp02[1:len(temp02)].find('+')+1]
            current_consumption = Decimal(consumption) - previus_consumption
            list_time.append(time_hour)
            list_current_consumption.append(current_consumption)
            previus_consumption = Decimal(consumption)
    #Close File
    all_consumption.close()
    return list_current_consumption


def extract_energy_in_string(string):
    string = string.split("+")
    return string[1]


def get_file_last_line(path_and_name_file):
    file_consumption = open(path_and_name_file)
    file_lines = file_consumption.readlines()
    last_line = file_lines[len(file_lines) - 1]
    file_consumption.close()
    return last_line


def extract_total_consumption_house(path_and_name_file):
    last_line = get_file_last_line(path_and_name_file)
    energy = extract_energy_in_string(last_line)
    return energy


def extract_coupled_consumption_house_per_hour(path_and_name_file):
    file_consumption = open(path_and_name_file)
    list_consumption = []
    for line in file_consumption:
        if line[0] != "#":
            list_consumption.append(extract_energy_in_string(line))
    file_consumption.close()
    return list_consumption


def extract_consumption_house_per_hour(path_and_name_file):
    file_consumption = open(path_and_name_file)
    list_consumption = []
    previous_consumption = 0
    for line in file_consumption:
        if line[0] != "#":
            consumption = extract_energy_in_string(line)
            current_consumption = Decimal(consumption) - previous_consumption
            list_consumption.append(str(current_consumption))
            previous_consumption = Decimal(consumption)
    file_consumption.close()
    return list_consumption


def sum_consumption_list(list_consumption):
    sum = 0
    for i in range(len(list_consumption)):
        sum += Decimal(list_consumption[i])
    return sum


def get_path_data_gridlab_files():
    return os.path.join(os.getcwd(), "data_gridlab")


def write_data_file_house_per_hour(path, number_houses):
    list_name_houses = ["house" + str(i + 1) + "output.csv" for i in range(number_houses)]
    Path("./data_gridlab").mkdir(exist_ok=True)
    file_data_csv = csv.writer(open("data_gridlab/houses_consumption_per_hour.csv", "w"))
    file_data_csv.writerow(["hour" + str(i) for i in range(25)]) #25 pra pegar o ultimo energy da hora
    for i in range(len(list_name_houses)):
        name_house_file = list_name_houses[i]
        current_path = os.path.join(glm_build.get_path_gridlab_temp_files(), name_house_file)
        file_data_csv.writerow(extract_consumption_house_per_hour(current_path))


def write_data_file_all_appliance_of_house_per_hour(path, list_houses):
    Path("./data_gridlab").mkdir(exist_ok=True)
    file_data_csv = csv.writer(open("data_gridlab/houses_consumption_per_hour_temp.csv", "w"))
    file_data_csv.writerow(["hour" + str(i) for i in range(25)])  # 25 pra pegar o ultimo energy da hora
    list_appliance_energy = []
    for i in range(len(list_houses)):
        for j in range(len(list_houses[i].get_list_appliances())):
            name_appliance = list_houses[i].get_list_appliances()[j].get_name()
            name_appliance = name_appliance + "rec.csv"
            current_path = os.path.join(glm_build.get_path_gridlab_temp_files(), name_appliance)
            #file_data_csv.writerow(extract_consumption_house_per_hour(current_path))
            #file_data_csv.writerow([name_appliance, 1])
            list_appliance_energy.append(extract_consumption_house_per_hour(current_path))

    #list_appliance_energy_sum_per_hour = []
    #for k in range(len(list_appliance_energy)):






