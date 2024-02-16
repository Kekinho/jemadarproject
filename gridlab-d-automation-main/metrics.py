# -*- coding: utf-8 -*-

import pandas as pd
import csv
from pathlib import Path

peak_time = [18, 19, 20, 21]

def get_metrics():
    data = pd.read_csv("data_gridlab/houses_consumption_per_hour.csv")
    print(data.describe())
    #print("MAX")
    print(data.min())
    print("MAX: " + str(get_all_max(data.max())))
    print("MIN: " + str(get_all_min(data.min())))
    print("MAX peak: " + str(get_max_off_peak_time(data.max())))
    print("MIN peak: " + str(get_min_off_peak_time(data.min())))
    print("MEAN: " + str(get_all_mean(data.mean())))
    print("MEAN peak: " + str(get_mean_off_peak_time(data.mean())))
    init_files()
    write_one_step_results_all_time()
    write_one_step_results_off_peak_time()
    write_one_step_results_all_time()
    write_one_step_results_off_peak_time()
    #print(data)
    #print(len(data))


def init_files():
    file_data_csv_all = csv.writer(open("results/results_by_season_all_time.csv", "w"))
    file_data_csv_all.writerow(["max", "min", "mean", "max_all"])
    file_data_csv_peak = csv.writer(open("results/results_by_season_off_peak_time.csv", "w"))
    file_data_csv_peak.writerow(["max", "min", "mean", "max_all"])


def init_files2():
    file_data_csv_all = csv.writer(open("results/results_by_season_all_time.csv", "w"))
    file_data_csv_all.writerow(["max", "min", "mean", "max_all"])
    file_data_csv_peak = csv.writer(open("results/results_by_season_off_peak_time.csv", "w"))
    file_data_csv_peak.writerow(["max", "min", "mean", "max_all"])

def write_one_step_results_all_time():
    data = pd.read_csv("data_gridlab/houses_consumption_per_hour.csv")
    data = data.drop(['hour0'], axis=1)# HOUR 0 ALWAYS = 0
    Path("./results").mkdir(exist_ok=True)
    file_data_csv = csv.writer(open("results/results_by_season_all_time.csv", "a"))
    #print(data.min())
    list_results = [get_all_max(data.max()), get_all_min(data.min()), get_all_mean(data.mean()), get_sum_max(data.max())]
    file_data_csv.writerow(list_results)


def write_one_step_results_off_peak_time():
    data = pd.read_csv("data_gridlab/houses_consumption_per_hour.csv")
    data = data.drop(['hour0'], axis=1)# HOUR 0 ALWAYS = 0
    Path("./results").mkdir(exist_ok=True)
    file_data_csv = csv.writer(open("results/results_by_season_off_peak_time.csv", "a"))
    list_results = [get_max_off_peak_time(data.max()), get_min_off_peak_time(data.min()), get_mean_off_peak_time(data.mean()), get_sum_max(data.max())]
    file_data_csv.writerow(list_results)

def print_data():
    data = pd.read_csv("data_gridlab/houses_consumption_per_hour.csv")
    data = data.drop(['hour0'], axis=1)  # HOUR 0 ALWAYS = 0
    #print(data)


def get_all_max(list_max):
    max = 0
    for i in list_max:
        if i > max:
            max = i
    return max


def get_sum_max(list_max):
    sum = 0
    for i in list_max:
            sum += i
    return sum

def get_max_off_peak_time(list_max):
    max = 0
    for i in range(len(list_max)):
        if list_max[i] > max and i not in peak_time:
            max = list_max[i]
    return max


def get_sum_on_peak_time(list_max):
    sum = 0
    list_peak = list_max[17:20]
    for i in range(len(list_peak)):
        sum += list_peak[i]
    return sum


def get_all_min(list_min):
    min = 100000000
    for i in list_min:
        if i < min:
            min = i
    return min


def get_min_off_peak_time(list_min):
    min = 0
    for i in range(len(list_min)):
        if list_min[i] < min and i not in peak_time:
            min = list_min[i]
    return min


def get_all_mean(list_mean):
    sum = 0
    for i in range(len(list_mean)):
        sum += list_mean[i]
    return sum/len(list_mean)


def get_mean_off_peak_time(list_mean):
    sum = 0
    for i in range(len(list_mean)):
        if i not in peak_time:
            sum += list_mean[i]
    return sum/(len(list_mean) - len(peak_time))

#get_metrics()
