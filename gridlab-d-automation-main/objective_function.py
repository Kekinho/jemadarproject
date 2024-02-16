# -*- coding: utf-8 -*-
import numpy as np
from decimal import Decimal


def objective_function_on_off_peak(list):
    off_peak = coefficient_of_variation_off_peak_time(list)
    on_peak = weight_on_peak_time(list)
    result = (Decimal(off_peak) * Decimal(0.8)) + (Decimal(on_peak) * Decimal(0.2))
    return result


def coefficient_variation(list):
    if np.sum(list) > 0:
        return np.std(list)/np.mean(list)
    else:
        return 0


def coefficient_of_variation_off_peak_time(list):
    result = 0
    #print(list[0:17]+list[20:23])
    #print(list)
    return coefficient_variation(list[0:17]+list[20:23])


def weight_on_peak_time(list):
    #print(list[17:20])
    #print(list)
    sum_total = np.sum(list)
    #print("SUM TOTAL: " + str(sum_total))
    on_peak_sum = np.sum(list[17:20])
    #print("Soma no pico: " + str(on_peak_sum))
    normalized_value = 0
    if on_peak_sum > 0:
        normalized_value = (on_peak_sum - 0) / (sum_total - 0)
    #print("Valor Normalizado: " + str(normalized_value))
    return normalized_value

#list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
#list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 50, 50, 50, 1, 1, 1, 1]
#list3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#list4 = [0, Decimal(0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 0, 0, 0, 0]

#print(coefficient_of_variation(list))
#print(coefficient_of_variation(list2))

#print(coefficient_of_variation_off_peak_time(list2))
#c = weight_on_peak_time(list4)
#print(c)


#print("OBJECTIVE FUNCTION : " + str(objective_function_on_off_peak(list2)))