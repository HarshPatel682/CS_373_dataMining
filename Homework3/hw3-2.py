import urllib.request
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import csv
import pandas as pd
import sys


# file_handler = open("yelp2_train.csv", "r", encoding="utf-8")
# reader = csv.reader(file_handler)
# read_data = list(reader)
# file_handler.close


train_data = "train-set.csv"
test_data = "test-set.csv"
if len(sys.argv) >= 2:
    train_data = sys.argv[1]
    test_data = sys.argv[2]

# my_url = "https://www.cs.purdue.edu/homes/ribeirob/courses/Fall2017/data/yelp2_train.csv"
data = []
keys = []

file_handler = open(train_data, "r", encoding="utf-8")
reader = csv.reader(file_handler)
read_data = list(reader)
# print(len(read_data))

for i in range(len(read_data)):
    for j in range(len(read_data[i])):
        if read_data[i][j] == '':
            read_data[i][j] = 'NA'
            # print(read_data[i][j])
        else:
            continue

my_dict = {}
attributes_for_each_my_dict = {}
for i in range(len(read_data[0])):
    key = read_data[0][i]
    if key == 'latitude' or key == 'longitude' or key == 'reviewCount' or key == 'checkins':
        continue
    keys.append(key)
    # print(key)
    temp_array = []
    for j in range(len(read_data)):
        if j+1 != len(read_data):
            temp_array.append(read_data[j+1][i])
    my_dict[key] = temp_array

counts_for_goodForGroups_one = my_dict['goodForGroups'].count('1')
counts_for_goodForGroups_zero = my_dict['goodForGroups'].count('0')

attr_goodForGroups = ['0', '1']
for i in range(len(keys)):
    if keys[i] == 'goodForGroups':
        continue
    attributes_for_each_my_dict[keys[i]] = np.unique(my_dict[keys[i]])

attributes_counts_each_attribute_GFG_one = {}


for x in keys:
    if x == 'goodForGroups':
        continue
    for i in attributes_for_each_my_dict[x]:
        temp = x + '=' + i
        attributes_counts_each_attribute_GFG_one[temp] = 0

attributes_counts_each_attribute_GFG_zero = attributes_counts_each_attribute_GFG_one.copy()

for i in range(len(my_dict[keys[1]])):
    if my_dict['goodForGroups'][i] == '1':
        for j in attributes_for_each_my_dict: #thru the keys
            x = my_dict[j][i]
            temp = j + '=' + x
            attributes_counts_each_attribute_GFG_one[temp] += 1
    elif my_dict['goodForGroups'][i] == '0':
        for j in attributes_for_each_my_dict: #thru the keys
            x = my_dict[j][i]
            temp = j + '=' + x
            attributes_counts_each_attribute_GFG_zero[temp] += 1

# get percentage with smoothing(ex P(priceRange=1 | GFG=1) = 6086(+1)/13326(+5)) but with smoothing
attributes_counts_each_attribute_GFG_zero_percentage = attributes_counts_each_attribute_GFG_zero.copy()
attributes_counts_each_attribute_GFG_one_percentage = attributes_counts_each_attribute_GFG_zero.copy()

# **IMPORTANT** keys for this are stored as 'class=attribute'
for i in attributes_counts_each_attribute_GFG_zero:
    temp = i.partition('=')
    length = len(attributes_for_each_my_dict[temp[0]])
    # if temp[0] == 'priceRange': # for TESTING PURPOSES
    #     print(attributes_counts_each_attribute_GFG_zero[i])
    attributes_counts_each_attribute_GFG_zero_percentage[i] = (attributes_counts_each_attribute_GFG_zero[i] +1)/(counts_for_goodForGroups_zero+length)
    attributes_counts_each_attribute_GFG_one_percentage[i] = (attributes_counts_each_attribute_GFG_one[i] +1)/(counts_for_goodForGroups_zero+length)

file_handler = open(test_data, "r", encoding="utf-8")
reader = csv.reader(file_handler)
new_read_data = list(reader)
# print(len(new_read_data))

dict_test_all = {}

for i in range(len(new_read_data)):
    for j in range(len(new_read_data[i])):
        if new_read_data[i][j] == '':
            new_read_data[i][j] = 'NA'

test_data_GFG = [new_read_data[x][0] for x in range(len(new_read_data))]
test_data_GFG_dict = {}
test_data_GFG_dict[test_data_GFG[0]] = test_data_GFG[1::]
# print(len(test_data_GFG_dict['goodForGroups']))
# exit(1)

test_keys = []
my_dict_test = {}
attributes_for_each_my_dict_test = {}
for i in range(len(new_read_data[0])):
    key = new_read_data[0][i]
    if key == 'latitude' or key == 'longitude' or key == 'reviewCount' or key == 'checkins':
        continue
    test_keys.append(key)
    # print(key)
    temp_array = []
    for j in range(len(read_data)):
        if j+1 != len(read_data):
            temp_array.append(read_data[j+1][i])
    my_dict_test[key] = temp_array

for i in range(len(test_keys)):
    if test_keys[i] == 'goodForGroups':
        continue
    attributes_for_each_my_dict_test[test_keys[i]] = np.unique(my_dict_test[test_keys[i]])

# print(attributes_for_each_my_dict_test)
# exit(1)
test_classes_without_GFG = [x for x in new_read_data[0]]
classes_to_remove = ['goodForGroups', 'latitude', 'longitude', 'reviewCount', 'checkins']
for x in classes_to_remove:
    test_classes_without_GFG.remove(x)

# dict_test_all = {}
test_data_predictions_GFG = []

num_gfg_zero_in_test = test_data_GFG_dict['goodForGroups'].count('0')
num_gfg_one_in_test = test_data_GFG_dict['goodForGroups'].count('1')

for i in range(len(new_read_data)):
    if i == 0:
        continue
    temp_array = new_read_data[i][1::]
    temp_gfg_one_value = 0
    temp_gfg_zero_value = 0

    temp_city = 'city=' + temp_array[0]
    temp_state = 'state=' + temp_array[1]
    temp_stars = 'stars=' + temp_array[4]
    temp_open = 'open=' + temp_array[7]
    temp_alcohol = 'alcohol=' + temp_array[8]
    temp_noiseLevel = 'noiseLevel=' + temp_array[9]
    temp_attire = 'attire=' + temp_array[10]
    temp_priceRange = 'priceRange=' + temp_array[11]
    temp_delivery = 'delivery=' + temp_array[12]
    temp_waiterService = 'waiterService=' + temp_array[13]
    temp_smoking = 'smoking=' + temp_array[14]
    temp_outdoorSeating = 'outdoorSeating=' + temp_array[15]
    temp_caters = 'caters=' + temp_array[16]
    temp_goodForKids = 'goodForKids=' + temp_array[17]

    array_of_above = []
    array_of_above.append(temp_city)
    array_of_above.append(temp_state)
    array_of_above.append(temp_stars)
    array_of_above.append(temp_city)
    array_of_above.append(temp_open)
    array_of_above.append(temp_alcohol)
    array_of_above.append(temp_noiseLevel)
    array_of_above.append(temp_attire)
    array_of_above.append(temp_priceRange)
    array_of_above.append(temp_delivery)
    array_of_above.append(temp_waiterService)
    array_of_above.append(temp_smoking)
    array_of_above.append(temp_outdoorSeating)
    array_of_above.append(temp_caters)
    array_of_above.append(temp_goodForKids)


    for x in array_of_above:
        if temp_gfg_one_value == 0:
            if x not in attributes_counts_each_attribute_GFG_one_percentage:
                splits = x.partition('=')
                temp_gfg_one_value += 1 / (num_gfg_one_in_test+(len(attributes_for_each_my_dict_test[splits[0]])))
            else:
                temp_gfg_one_value += attributes_counts_each_attribute_GFG_one_percentage[x]
        else:
            if x not in attributes_counts_each_attribute_GFG_one_percentage:
                splits = x.partition('=')
                temp_gfg_one_value *= 1 / num_gfg_one_in_test+(len(attributes_for_each_my_dict_test[splits[0]]))
            else:
                temp_gfg_one_value *= attributes_counts_each_attribute_GFG_one_percentage[x]

    for x in array_of_above:
        if temp_gfg_zero_value == 0:
            if x not in attributes_counts_each_attribute_GFG_zero_percentage:
                splits = x.partition('=')
                temp_gfg_zero_value += 1 / (num_gfg_zero_in_test + len(attributes_for_each_my_dict_test[splits[0]]))
            else:
                temp_gfg_zero_value += attributes_counts_each_attribute_GFG_zero_percentage[x]
        else:
            if x not in attributes_counts_each_attribute_GFG_one_percentage:
                splits = x.partition('=')
                temp_gfg_zero_value *= 1 / (num_gfg_zero_in_test + len(attributes_for_each_my_dict_test[splits[0]]))
            else:
                temp_gfg_zero_value *= attributes_counts_each_attribute_GFG_one_percentage[x]


    if temp_gfg_zero_value > temp_gfg_one_value:
        test_data_predictions_GFG.append('0')
    else:
        test_data_predictions_GFG.append('1')

zero_one_loss = 0
for i in range(len(test_data_predictions_GFG)):
    if test_data_GFG_dict['goodForGroups'][i] != test_data_predictions_GFG[i]:
        zero_one_loss += 1
zero_one_loss = zero_one_loss/len(test_data_predictions_GFG)
print("ZERO-ONE LOSS =", zero_one_loss)


# squared_loss = 0
predictions_count_one = test_data_predictions_GFG.count('1')
predictions_count_zero = test_data_predictions_GFG.count('0')

squared_loss = (1 - (predictions_count_one/(predictions_count_one+predictions_count_zero)))**2
squared_loss += (1 - (predictions_count_zero/(predictions_count_one+predictions_count_zero)))**2
squared_loss = squared_loss/2
print('SQUARED LOSS = ', squared_loss)