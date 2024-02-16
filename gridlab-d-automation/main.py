# -*- coding: utf-8 -*-
import copy

import build_microgrid as glm_mg
import build_gridlab_file as glm_build_file
import extract_data_gridlab as glm_ext
import clustering as glm_cluster
import build_schedule as glm_schedule
import workload as glm_workload
import optimization_algorithms as algorithms
import gridlab_lib as glm_lib
import metrics
import work_files
from optimization_algorithms import run_algorithm_group_schedule

number_of_houses = 20
number_of_appliances = 10
number_of_epochs_for_day = 1
number_of_groups = 20

# WORKLOAD, SCHEDULES ...
workload = glm_workload.Workload(number_of_houses, number_of_appliances)
# CASAS COM OS SCHEDULES
object_build_schedule_in_workload = glm_schedule.Build_Schedule(workload.get_workload())
# OUTPUT FORMAT: [0, 21, 1.5] ...
collections_house_random_schedules = object_build_schedule_in_workload.get_list_random_schedule_houses()

# init
# temp_schedules = algorithms.hill_climb_collections(house_random_schedules, 1)

# all_schedules = build_schedules.update_house_schedule_list(temp_schedules, build_schedules.get_list_houses())
# print(output)

################


def run_microgrid(days, collections_house_random_schedules, object_build_schedule_in_workload):
    #new_schedules = algorithms.hill_climb_collections(collections_house_random_schedules, 1)
    update_schedules = object_build_schedule_in_workload.update_house_schedule_list(collections_house_random_schedules,
                                                                                    object_build_schedule_in_workload.get_list_houses())
    temp = [collections_house_random_schedules, object_build_schedule_in_workload, update_schedules]
    for i in range(days):
        temp = run(temp[0], temp[1], temp[2])
        #print(temp[0])


def run(collections_house_random_schedules, build_schedules, update_schedules):

    #delete_files_in_folder
    #work_files.delete_files_in_folder_output_files_gridlab()
    #work_files.delete_files_in_folder_data_gridlab()

    collections_house_random_schedules_temp = copy.deepcopy(collections_house_random_schedules)
    update_schedules_temp = copy.deepcopy(update_schedules)
    # new_schedules = algorithms.hill_climb_collections(collections_house_random_schedules_temp, 1)
    # update_schedules = build_schedules.update_house_schedule_list(collections_house_random_schedules_temp,
    # build_schedules.get_list_houses())

    microgrid = glm_lib.Microgrid()
    microgrid.add_list_houses(build_schedules.get_list_houses())
    microgrid.add_list_schedules(update_schedules_temp)
    #print(microgrid)

    #var = microgrid.get_list_houses()[0].get_list_appliances()[0].get_name()

    #var2 = microgrid.get_list_houses()[0].list_appliances()[0].name()


    # write file
    glm_build_file.write_file_microgrid(microgrid)
    # run gridlab
    glm_build_file.run_gridlab_d_file()

    glm_ext.write_data_file_house_per_hour(glm_ext.get_path_data_gridlab_files(), number_of_houses)
    #glm_ext.write_data_file_all_appliance_of_house_per_hour(glm_ext.get_path_data_gridlab_files(), microgrid.get_list_houses())

    # cluster
    cluster_groups = glm_cluster.get_groups_org(number_of_groups)

    # algorithm HILL CLIMBING -> interations (number_of_groups)
    ###############################################################
    #hill_climbing_intrations = 1
    #group_output = algorithms.run_algorithm_group_schedule(collections_house_random_schedules_temp, hill_climbing_intrations,
    #                                                       cluster_groups,
    #                                                       algorithms.hill_climb_collections, number_of_houses)

    #GENETIC
    ##############################################################
    #genetic_interations = 1
    #group_output = algorithms.run_algorithm_group_schedule(collections_house_random_schedules_temp, genetic_interations,
    #                                                       cluster_groups,
    #                                                       algorithms.genetic_collections, number_of_houses)

    group_output = algorithms.run_algorithm(collections_house_random_schedules_temp,
                                                           algorithms.hill_climb, number_of_epochs_for_day)

    #group_output = algorithms.run_algorithm_group_schedule(collections_house_random_schedules_temp, 1, cluster_groups,
    #                                                       algorithms.hill_climb_collections, number_of_houses)

    # update
    group_schedules_update = build_schedules.update_house_schedule_list(group_output,
                                                                 build_schedules.get_list_houses())

    # write metrics
    metrics.write_one_step_results_all_time()
    metrics.write_one_step_results_off_peak_time()
    #print(group_schedules_update)
    #print("QUALITY COLLECTIONS:" + str(algorithms.get_quality_collections(group_output)))
    return group_output, build_schedules, group_schedules_update


# temp = run(collections_house_random_schedules, build_schedules)
# run(temp[0], temp[1])

metrics.init_files2()

for i in range(5):
    run_microgrid(5, collections_house_random_schedules, object_build_schedule_in_workload)

#metrics.print_data()
