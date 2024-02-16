import math
from sklearn.cluster import KMeans
import pandas as pd


def get_groups(number_of_groups):
    data = pd.read_csv("data_gridlab/houses_consumption_per_hour.csv")
    kmeans = KMeans(n_clusters=number_of_groups, random_state=0)
    kmeans.fit(data)
    return kmeans.labels_


def get_groups_org(number_of_groups):
    list_groups = []
    groups = get_groups(number_of_groups)
    for i in range(number_of_groups):
        list_temp = []
        for j in range(len(groups)):
            if i == groups[j]:
                list_temp.append(j)
        list_groups.append(list_temp)
    return list_groups


#print(get_groups(5))
#print(get_groups_org(5))