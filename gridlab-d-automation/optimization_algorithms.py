# -*- coding: utf-8 -*-
import random
import copy

from numpy import trunc

import objective_function as ob
from decimal import Decimal
import build_schedule as schedule


# moved functions
def generate_random_schedule(appliance_id, number_of_hours, appliance_power):
    list_schedule = []
    for i in range(number_of_hours):
        list_schedule.append([appliance_id, random.randint(0, 23), appliance_power])
    return list_schedule


# Gera a lista com os agendamentos aleatorios

# moved functions
def generate_list_random_schedule(list_os_appliances):
    list_random_schedule = []
    count = 0  # id_schedule
    for i in list_os_appliances:
        list_random_schedule.append(generate_random_schedule(count, i[0], i[1]))
        count += 1
    return list_random_schedule


# moved functions
def get_clean_list_schedule_cost():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def add_list_schedule_in_solution(list_random_schedule):
    list_schedule_cost = get_clean_list_schedule_cost()
    for i in range(len(list_random_schedule)):
        for j in range(len(list_random_schedule[i])):
            list_schedule_cost[list_random_schedule[i][j][1]] += Decimal(list_random_schedule[i][j][2])
    return list_schedule_cost


def add_collection_schedule_in_soluton(collection_random_schedule):
    list_schedule_cost = get_clean_list_schedule_cost()
    for i in range(len(collection_random_schedule)):
        # print("I : " + str(collection_random_schedule[i]))
        for j in range(len(collection_random_schedule[i])):
            # print("J : " + str(collection_random_schedule[i][j]))
            for k in range(len(collection_random_schedule[i][j])):
                # print("K : " + str(collection_random_schedule[i][j][k]))
                list_schedule_cost[collection_random_schedule[i][j][k][1]] += Decimal(
                    collection_random_schedule[i][j][k][2])
    return list_schedule_cost


def get_quality(list_schedule_cost):
    return ob.objective_function_on_off_peak(list_schedule_cost)


def get_quality_schedule(list_random_schedule):
    return ob.objective_function_on_off_peak(add_list_schedule_in_solution(list_random_schedule))


def get_quality_collections(collections_random_schedule):
    sum = 0
    for i in range(len(collections_random_schedule)):
        sum += get_quality_schedule(collections_random_schedule[i])
    return sum, get_quality(add_collection_schedule_in_soluton(collections_random_schedule)), add_collection_schedule_in_soluton(collections_random_schedule)


def compare_quality(list_schedule_cost_x, list_schedule_cost_y):
    calc_x = ob.objective_function_on_off_peak(list_schedule_cost_x)
    calc_y = ob.objective_function_on_off_peak(list_schedule_cost_y)
    if calc_x > calc_y:
        #print("QUALITY Y: " + str(calc_y))
        return True
    else:
        #print("QUALITY X: " + str(calc_x))
        return False


def compare_quality_schedule(list_random_schedule_x, list_random_schedule_y):
    list_schedule_cost_x = add_list_schedule_in_solution(list_random_schedule_x)
    list_schedule_cost_y = add_list_schedule_in_solution(list_random_schedule_y)
    if compare_quality(list_schedule_cost_x, list_schedule_cost_y):
        return True
    else:
        return False


def compare_quality_collections_schedule(collection_random_schedule_x, collection_random_schedule_y):
    collections_schedule_cost_x = add_collection_schedule_in_soluton(collection_random_schedule_x)
    collections_schedule_cost_y = add_collection_schedule_in_soluton(collection_random_schedule_y)
    if compare_quality(collections_schedule_cost_x, collections_schedule_cost_y):
        return True
    else:
        return False


def get_number_of_appliances_and_schedules(list_random_schedule):
    number_of_appliances = len(list_random_schedule)
    list_number_of_appliances_schedules = []
    for i in range(number_of_appliances):
        list_number_of_appliances_schedules.append(len(list_random_schedule[i]))
    return [number_of_appliances, list_number_of_appliances_schedules]


def new_random_int_no_repeat(list_appliances):
    list_deny_hour = []
    list_temp = []
    #print("PROBLEMA TWEAK")
    for i in range(len(list_appliances)):
        list_temp.append(list_appliances[i])
    #print(str(list_temp))
    for j in range(len(list_temp)):
        list_deny_hour.append(list_temp[j][1])

    flag = True
    new_random_int = -1
    while(flag):
        new_random_int = random.randint(0, 23)
        if not new_random_int is list_deny_hour:
            flag = False
    return new_random_int


#list_random_schedule[random_tweak_appliance]

def tweak(list_random_schedule):
    list_random_schedule_temp = copy.deepcopy(list_random_schedule)
    number_of_appliances_and_schedules = get_number_of_appliances_and_schedules(list_random_schedule_temp)
    number_of_appliances = number_of_appliances_and_schedules[0]
    list_number_of_appliances_schedules = number_of_appliances_and_schedules[1]
    random_tweak_appliance = random.randint(0, number_of_appliances - 1)
    random_tweak_appliance_schedule = random.randint(0, list_number_of_appliances_schedules[random_tweak_appliance] - 1)
    #new_random_schedule_hour = random.randint(0, 23)
    new_random_schedule_hour = new_random_int_no_repeat(list_random_schedule_temp[random_tweak_appliance])
    # print(random_tweak_appliance, random_tweak_appliance_schedule, new_random_schedule_hour)
    # print("ORIGINAL:" + str(list_random_schedule))
    ## EVITAR PROBLEMA DO TWAEK
    #new_random_int_no_repeat(list_random_schedule_temp[random_tweak_appliance])
    ##
    #var = list_random_schedule_temp[random_tweak_appliance][random_tweak_appliance_schedule][1]
    list_random_schedule_temp[random_tweak_appliance][random_tweak_appliance_schedule][1] = new_random_schedule_hour
    # print("TEMP:    " + str(list_random_schedule_temp))
    return list_random_schedule_temp


# O vetor de soluções deve conter os eletrodomésticos
def hill_climb(list_random_schedule, interations):
    list_random_schedule_temp_1 = copy.deepcopy(list_random_schedule)
    for i in range(interations):
        list_random_schedule_temp_2 = tweak(list_random_schedule_temp_1)
        # print("XXXXXXXXXX")
        # print("HILL CLIMBING 1: " + str(list_random_schedule_temp_1))
        # print("HILL CLIMBING 2: " + str(list_random_schedule_temp_2))
        if not compare_quality_schedule(list_random_schedule_temp_2, list_random_schedule_temp_1):
            list_random_schedule_temp_1 = copy.deepcopy(list_random_schedule_temp_2)
            # print(compare_quality_schedule(list_random_schedule_temp_1, list_random_schedule_temp_2))
            # print("TROCA")
    # print(list_random_schedule_temp_1)
    return list_random_schedule_temp_1


def hill_climb_collections(collections_schedule, interations):
    collections_schedule_temp_1 = copy.deepcopy(collections_schedule)

    for i in range(interations):
        collections_schedule_temp_2 = copy.deepcopy(collections_schedule_temp_1)
        # tweak
        for j in range(len(collections_schedule)):
            collections_schedule_temp_2[j] = tweak(collections_schedule_temp_1[j])

        if not compare_quality_collections_schedule(collections_schedule_temp_2, collections_schedule_temp_1):
            for k in range(len(collections_schedule)):
                collections_schedule_temp_1[k] = copy.deepcopy(collections_schedule_temp_2[k])
    return collections_schedule_temp_1


def genetic_collections(collections_schedule, interations):
    collections_schedule_temp_1 = copy.deepcopy(collections_schedule)

    for i in range(interations):
        collections_schedule_temp_2 = copy.deepcopy(collections_schedule_temp_1)
        # tweak
        for j in range(len(collections_schedule)):
            collections_schedule_temp_2[j] = genetic(collections_schedule_temp_1[j], 30, 100)

        if not compare_quality_collections_schedule(collections_schedule_temp_2, collections_schedule_temp_1):
            for k in range(len(collections_schedule)):
                collections_schedule_temp_1[k] = copy.deepcopy(collections_schedule_temp_2[k])
    return collections_schedule_temp_1


def run_algorithm(collections_all_schedules, optimization_algorithm, interations):
    list_output = []
    for i in range(len(collections_all_schedules)):
        list_output.append(optimization_algorithm(collections_all_schedules[i], interations))
    return list_output


def run_algorithm_group_schedule(collections_all_schedules, interations, group_schedule_lists, optimization_algorithm, number_of_houses):
    #print("NUMBER INTERATIONS: " + str(interations))
    list_schedules_grouped = []
    var = len(group_schedule_lists)
    for i in range(len(group_schedule_lists)):
        list_temp = []
        for j in range(len(group_schedule_lists[i])):
            list_temp.append(collections_all_schedules[i])
        list_schedules_grouped.append(list_temp)
    var = len(list_schedules_grouped)
    list_schedules_output = []
    for k in range(len(list_schedules_grouped)):
        var2 = list_schedules_grouped[k]
        list_schedules_output.append(optimization_algorithm(list_schedules_grouped[k], interations))

    #var88 = group_schedule_lists
    #list_final = [0 for i in range(number_of_houses)]
    list_final = []
    #print("SCHEDULES OUTPUT: " + str(list_schedules_output))
    for i in range(len(list_schedules_output)):
        for j in range(len(list_schedules_output[i])):
            list_final.append(list_schedules_output[i][j])
    #print("FINAL OUTPUT: " + str(list_final))
    return list_final


def run_algorithm_in_schedules(house_schedules, interations, optimization_algorithm):
    list_house_schedules = []
    for i in range(len(house_schedules)):
        temp_schedule = optimization_algorithm(house_schedules[i], interations)
        list_house_schedules.append(temp_schedule)
    return list_house_schedules


def run_otimization_algoritm(list_appliance, interations, optimization_algorithm):
    list_random_schedule = generate_list_random_schedule(list_appliance)
    #print(list_random_schedule)
    #print(add_list_schedule_in_solution(list_random_schedule))
    #print(get_quality(add_list_schedule_in_solution(list_random_schedule)))
    #print("XXXXXXXXXXXX")
    list_random_schedule = optimization_algorithm(list_random_schedule, interations)
    #print(get_quality(add_list_schedule_in_solution(list_random_schedule)))
    #print(add_list_schedule_in_solution(list_random_schedule))
    #print(list_random_schedule)
    return list_random_schedule


# GENETIC
def crossover_wrong(list_random_schedule):
    #print(list_random_schedule)
    list_chromosome = []
    for i in range(len(list_random_schedule)):
        for j in range(len(list_random_schedule[i])):
            list_chromosome.append(list_random_schedule[i][j][1])
    #print(list_chromosome)

    list_chromosome_revert = copy.deepcopy(list_chromosome[::-1])
    list_random_schedule_cross = copy.deepcopy(list_random_schedule)
    count = 0
    for i in range(len(list_random_schedule_cross)):
        for j in range(len(list_random_schedule_cross[i])):
            #print(count)
            list_random_schedule_cross[i][j][1] = list_chromosome_revert[count]
            count += 1
    #print(list_chromosome_revert)
    #print(list_random_schedule_cross)
    return list_random_schedule_cross


def crossover(list_random_schedule_x, list_random_schedule_y):
    list_hour_chromosome_x = []
    list_hour_chromosome_y = []
    for i in range(len(list_random_schedule_x)):
        for j in range(len(list_random_schedule_x[i])):
            list_hour_chromosome_x.append(list_random_schedule_x[i][j][1])
            list_hour_chromosome_y.append(list_random_schedule_y[i][j][1])
    #print(list_hour_chromosome_x)
    #print(list_hour_chromosome_y)

    #print(list_random_schedule_x)
    #print(list_random_schedule_y)

    for i in range(int(len(list_hour_chromosome_x)/2)):
        temp = list_hour_chromosome_x[i]
        list_hour_chromosome_x[i] = list_hour_chromosome_y[i]
        list_hour_chromosome_y[i] = temp

    #print("XXXXXXXXXXXXXXXXXXX")
    #print(list_hour_chromosome_x)
    #print(list_hour_chromosome_y)

    count = 0
    for i in range(len(list_random_schedule_x)):
        for j in range(len(list_random_schedule_x[i])):
            # print(count)
            list_random_schedule_x[i][j][1] = list_hour_chromosome_x[count]
            list_random_schedule_y[i][j][1] = list_hour_chromosome_y[count]
            count += 1

    #print(list_random_schedule_x)
    #print(list_random_schedule_y)
    return list_random_schedule_x, list_random_schedule_y

def generate_solution_candidate(list_random_schedule):
    list_random_schedule_temp = copy.deepcopy(list_random_schedule)
    list_new_hour = [random.randint(0, 23) for i in range(200)] #MUDANÇA -> vetor de numeros aleatorios
    #print("YYYYYYYYYYYYYY")
    #print(list_new_hour)
    #print(len(list_new_hour))
    #print(list_random_schedule)
    count = 0
    for i in range(len(list_random_schedule_temp)):
        for j in range(len(list_random_schedule_temp[i])):
            # print(count)
            list_random_schedule_temp[i][j][1] = list_new_hour[count]
            count += 1
    #print(list_random_schedule)
    #print(list_random_schedule_temp)
    return list_random_schedule_temp


def generate_initial_population(list_random_schedule, number_of_solutions):
    list_population = []
    for i in range(number_of_solutions):
        list_population.append(generate_solution_candidate(list_random_schedule))
    return list_population


def sorted_population(collections_list_random_schedule):
    #print(collections_list_random_schedule)
    collections_list_random_schedule_sorted = copy.deepcopy(collections_list_random_schedule)
    collections_list_random_schedule_sorted = sorted(collections_list_random_schedule_sorted, key=get_quality_schedule)
    #print(collections_list_random_schedule_sorted)
    return collections_list_random_schedule_sorted

def genetic(list_random_schedule, population_size, interations):
    list_random_schedule_temp = copy.deepcopy(list_random_schedule)
    best = copy.deepcopy(list_random_schedule)
    population = generate_initial_population(best, population_size)
    # LAÇO AQUI
    for i in range(interations):
        population_best = sorted_population(population)[0]

        if get_quality_schedule(best) > get_quality_schedule(population_best):
            best = copy.deepcopy(population_best)

        for i in range(int(population_size / 2)):
            population_solution_x = population[random.randint(0, population_size - 1)]
            population_solution_y = population[random.randint(0, population_size - 1)]
            childless = crossover(population_solution_x, population_solution_y)
            x = childless
            population.append(tweak(childless[0]))
            population.append(tweak(childless[1]))

        population = sorted_population(population)[0:population_size]
    return best



list_appliance = [[2, 1], [1, 2], [5, 1.5], [7, 1.7], [3, 2.3], [1, 7], [1, 5.3]]
#list_appliance = [[2, 1.5], [1, 2.6], [1, 6.5]]
#list_appliance = [[2, 1.5], [1, 2.6]]
# print(len(solution_list))

hc = run_otimization_algoritm(list_appliance, 100, hill_climb)

list_random_schedule11 = generate_list_random_schedule(list_appliance)
list_random_schedule22 = generate_list_random_schedule(list_appliance)
#print("XXXXXXXXXXXXXXXXXXXXXX")
#print(list_random_schedule11)

#print(crossover(list_random_schedule11))
#print(generate_solution_candidate(list_random_schedule11))
population = generate_initial_population(list_random_schedule11, 10)
#print(population)
#print(get_quality_schedule(population[0]))
s_population = sorted_population(population)
#print(get_quality_schedule(s_population[0]))

#crossover(s_population[0], s_population[1])
genetic(s_population[0], 10, 10)

collections_schedule = [list_random_schedule11, list_random_schedule22]
#print(list_random_schedule11)
#print(list_random_schedule22)
#print(get_quality_schedule(list_random_schedule11) + get_quality_schedule(list_random_schedule22))

collections_schedule_output = hill_climb_collections(collections_schedule, 50)

#print(collections_schedule_output[0])
#print(collections_schedule_output[1])
#print(get_quality_schedule(collections_schedule_output[0]) + get_quality_schedule(collections_schedule_output[1]))

solution = add_collection_schedule_in_soluton(collections_schedule)
#print(solution)

#import clustering

#groups = clustering.get_groups_org(2)
#print(groups)

#output_group = run_algorithm_group_schedule(collections_schedule, 2, groups, hill_climb_collections)
#print(output_group)
#print(output_group[0])
#print(output_group[1])