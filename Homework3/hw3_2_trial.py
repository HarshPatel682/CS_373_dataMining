import random
import urllib.request
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import csv
import random
import sys

# split_percentages = [.01, .1, .5]
#
#
# for num in range(10):
#     split_data_percentage = .5
#     file_handler = open("yelp2_train.csv", "r", encoding="utf-8")
#     reader = csv.reader(file_handler)
#     read_data = list(reader)
#     num_of_rows_in_train = int(len(read_data)*split_data_percentage)
#     num_of_rows_in_test = int(len(read_data) - num_of_rows_in_train)-1
#
#     random_values_for_train = []
#     i = 0
#     while i < num_of_rows_in_train:
#         temp_random_number = random.randint(1, len(read_data))
#         if temp_random_number not in random_values_for_train:
#             random_values_for_train.append(temp_random_number)
#             i += 1
#     i = 0
#     # print(len(random_values_for_train))
#     with open("train-set.csv", "w", newline='') as file:
#         file_writer = csv.writer(file)
#         file_writer.writerow(read_data[0])
#         for k in range(len(random_values_for_train)):
#             file_writer.writerow(read_data[random_values_for_train[k]])
#     file.close()
#
#     with open("test-set.csv", "w", newline='') as file:
#         file_writer = csv.writer(file)
#         file_writer.writerow(read_data[0])
#         for k in range(len(read_data)):
#             if random_values_for_train.__contains__(k) or k == 0:
#                 continue
#             file_writer.writerow(read_data[k])
#
#     file.close()
#
#     train_data = "train-set.csv"
#     test_data = "test-set.csv"
#
#
#
#     # my_url = "https://www.cs.purdue.edu/homes/ribeirob/courses/Fall2017/data/yelp2_train.csv"
#     data = []
#     keys = []
#
#     file_handler = open(train_data, "r", encoding="utf-8")
#     reader = csv.reader(file_handler)
#     read_data = list(reader)
#     # print(len(read_data))
#
#     for i in range(len(read_data)):
#         for j in range(len(read_data[i])):
#             if read_data[i][j] == '':
#                 read_data[i][j] = 'NA'
#                 # print(read_data[i][j])
#             else:
#                 continue
#
#     my_dict = {}
#     attributes_for_each_my_dict = {}
#     for i in range(len(read_data[0])):
#         key = read_data[0][i]
#         if key == 'latitude' or key == 'longitude' or key == 'reviewCount' or key == 'checkins':
#             continue
#         keys.append(key)
#         # print(key)
#         temp_array = []
#         for j in range(len(read_data)):
#             if j+1 != len(read_data):
#                 temp_array.append(read_data[j+1][i])
#         my_dict[key] = temp_array
#
#     counts_for_goodForGroups_one = my_dict['goodForGroups'].count('1')
#     counts_for_goodForGroups_zero = my_dict['goodForGroups'].count('0')
#
#     attr_goodForGroups = ['0', '1']
#     for i in range(len(keys)):
#         if keys[i] == 'goodForGroups':
#             continue
#         attributes_for_each_my_dict[keys[i]] = np.unique(my_dict[keys[i]])
#
#     attributes_counts_each_attribute_GFG_one = {}
#
#
#     for x in keys:
#         if x == 'goodForGroups':
#             continue
#         for i in attributes_for_each_my_dict[x]:
#             temp = x + '=' + i
#             attributes_counts_each_attribute_GFG_one[temp] = 0
#
#     attributes_counts_each_attribute_GFG_zero = attributes_counts_each_attribute_GFG_one.copy()
#
#     for i in range(len(my_dict[keys[1]])):
#         if my_dict['goodForGroups'][i] == '1':
#             for j in attributes_for_each_my_dict: #thru the keys
#                 x = my_dict[j][i]
#                 temp = j + '=' + x
#                 attributes_counts_each_attribute_GFG_one[temp] += 1
#         elif my_dict['goodForGroups'][i] == '0':
#             for j in attributes_for_each_my_dict: #thru the keys
#                 x = my_dict[j][i]
#                 temp = j + '=' + x
#                 attributes_counts_each_attribute_GFG_zero[temp] += 1
#
#     # get percentage with smoothing(ex P(priceRange=1 | GFG=1) = 6086(+1)/13326(+5)) but with smoothing
#     attributes_counts_each_attribute_GFG_zero_percentage = attributes_counts_each_attribute_GFG_zero.copy()
#     attributes_counts_each_attribute_GFG_one_percentage = attributes_counts_each_attribute_GFG_zero.copy()
#
#     # **IMPORTANT** keys for this are stored as 'class=attribute'
#     for i in attributes_counts_each_attribute_GFG_zero:
#         temp = i.partition('=')
#         length = len(attributes_for_each_my_dict[temp[0]])
#         # if temp[0] == 'priceRange': # for TESTING PURPOSES
#         #     print(attributes_counts_each_attribute_GFG_zero[i])
#         attributes_counts_each_attribute_GFG_zero_percentage[i] = (attributes_counts_each_attribute_GFG_zero[i] +1)/(counts_for_goodForGroups_zero+length)
#         attributes_counts_each_attribute_GFG_one_percentage[i] = (attributes_counts_each_attribute_GFG_one[i] +1)/(counts_for_goodForGroups_zero+length)
#
#     file_handler = open(test_data, "r", encoding="utf-8")
#     reader = csv.reader(file_handler)
#     new_read_data = list(reader)
#     # print(len(new_read_data))
#
#     dict_test_all = {}
#
#     for i in range(len(new_read_data)):
#         for j in range(len(new_read_data[i])):
#             if new_read_data[i][j] == '':
#                 new_read_data[i][j] = 'NA'
#
#     test_data_GFG = [new_read_data[x][0] for x in range(len(new_read_data))]
#     test_data_GFG_dict = {}
#     test_data_GFG_dict[test_data_GFG[0]] = test_data_GFG[1::]
#     # print(len(test_data_GFG_dict['goodForGroups']))
#     # exit(1)
#
#     test_keys = []
#     my_dict_test = {}
#     attributes_for_each_my_dict_test = {}
#     for i in range(len(new_read_data[0])):
#         key = new_read_data[0][i]
#         if key == 'latitude' or key == 'longitude' or key == 'reviewCount' or key == 'checkins':
#             continue
#         test_keys.append(key)
#         # print(key)
#         temp_array = []
#         for j in range(len(read_data)):
#             if j+1 != len(read_data):
#                 temp_array.append(read_data[j+1][i])
#         my_dict_test[key] = temp_array
#
#     for i in range(len(test_keys)):
#         if test_keys[i] == 'goodForGroups':
#             continue
#         attributes_for_each_my_dict_test[test_keys[i]] = np.unique(my_dict_test[test_keys[i]])
#
#     # print(attributes_for_each_my_dict_test)
#     # exit(1)
#     test_classes_without_GFG = [x for x in new_read_data[0]]
#     classes_to_remove = ['goodForGroups', 'latitude', 'longitude', 'reviewCount', 'checkins']
#     for x in classes_to_remove:
#         test_classes_without_GFG.remove(x)
#
#     # dict_test_all = {}
#     test_data_predictions_GFG = []
#
#     num_gfg_zero_in_test = test_data_GFG_dict['goodForGroups'].count('0')
#     num_gfg_one_in_test = test_data_GFG_dict['goodForGroups'].count('1')
#
#     for i in range(len(new_read_data)):
#         if i == 0:
#             continue
#         temp_array = new_read_data[i][1::]
#         temp_gfg_one_value = 0
#         temp_gfg_zero_value = 0
#
#         temp_city = 'city=' + temp_array[0]
#         temp_state = 'state=' + temp_array[1]
#         temp_stars = 'stars=' + temp_array[4]
#         temp_open = 'open=' + temp_array[7]
#         temp_alcohol = 'alcohol=' + temp_array[8]
#         temp_noiseLevel = 'noiseLevel=' + temp_array[9]
#         temp_attire = 'attire=' + temp_array[10]
#         temp_priceRange = 'priceRange=' + temp_array[11]
#         temp_delivery = 'delivery=' + temp_array[12]
#         temp_waiterService = 'waiterService=' + temp_array[13]
#         temp_smoking = 'smoking=' + temp_array[14]
#         temp_outdoorSeating = 'outdoorSeating=' + temp_array[15]
#         temp_caters = 'caters=' + temp_array[16]
#         temp_goodForKids = 'goodForKids=' + temp_array[17]
#
#         array_of_above = []
#         array_of_above.append(temp_city)
#         array_of_above.append(temp_state)
#         array_of_above.append(temp_stars)
#         array_of_above.append(temp_city)
#         array_of_above.append(temp_open)
#         array_of_above.append(temp_alcohol)
#         array_of_above.append(temp_noiseLevel)
#         array_of_above.append(temp_attire)
#         array_of_above.append(temp_priceRange)
#         array_of_above.append(temp_delivery)
#         array_of_above.append(temp_waiterService)
#         array_of_above.append(temp_smoking)
#         array_of_above.append(temp_outdoorSeating)
#         array_of_above.append(temp_caters)
#         array_of_above.append(temp_goodForKids)
#
#
#         for x in array_of_above:
#             if temp_gfg_one_value == 0:
#                 if x not in attributes_counts_each_attribute_GFG_one_percentage:
#                     splits = x.partition('=')
#                     temp_gfg_one_value += 1 / (num_gfg_one_in_test+(len(attributes_for_each_my_dict_test[splits[0]])))
#                 else:
#                     temp_gfg_one_value += attributes_counts_each_attribute_GFG_one_percentage[x]
#             else:
#                 if x not in attributes_counts_each_attribute_GFG_one_percentage:
#                     splits = x.partition('=')
#                     temp_gfg_one_value *= 1 / num_gfg_one_in_test+(len(attributes_for_each_my_dict_test[splits[0]]))
#                 else:
#                     temp_gfg_one_value *= attributes_counts_each_attribute_GFG_one_percentage[x]
#
#         for x in array_of_above:
#             if temp_gfg_zero_value == 0:
#                 if x not in attributes_counts_each_attribute_GFG_zero_percentage:
#                     splits = x.partition('=')
#                     temp_gfg_zero_value += 1 / (num_gfg_zero_in_test + len(attributes_for_each_my_dict_test[splits[0]]))
#                 else:
#                     temp_gfg_zero_value += attributes_counts_each_attribute_GFG_zero_percentage[x]
#             else:
#                 if x not in attributes_counts_each_attribute_GFG_one_percentage:
#                     splits = x.partition('=')
#                     temp_gfg_zero_value *= 1 / (num_gfg_zero_in_test + len(attributes_for_each_my_dict_test[splits[0]]))
#                 else:
#                     temp_gfg_zero_value *= attributes_counts_each_attribute_GFG_one_percentage[x]
#
#
#         if temp_gfg_zero_value > temp_gfg_one_value:
#             test_data_predictions_GFG.append('0')
#         else:
#             test_data_predictions_GFG.append('1')
#
#     zero_one_loss = 0
#     for i in range(len(test_data_predictions_GFG)):
#         if test_data_GFG_dict['goodForGroups'][i] != test_data_predictions_GFG[i]:
#             zero_one_loss += 1
#     zero_one_loss = zero_one_loss/len(test_data_predictions_GFG)
#     print("ZERO-ONE LOSS =", zero_one_loss)
#
#
#     # squared_loss = 0
#     predictions_count_one = test_data_predictions_GFG.count('1')
#     predictions_count_zero = test_data_predictions_GFG.count('0')
#
#     squared_loss = (1 - (predictions_count_one/(predictions_count_one+predictions_count_zero)))**2
#     squared_loss += (1 - (predictions_count_zero/(predictions_count_one+predictions_count_zero)))**2
#     squared_loss = squared_loss/2
#     print('SQUARED LOSS =', squared_loss)

zero_loss_1 = [0.36378787878787877,0.33934343434343434,0.3413131313131313,0.3527777777777779,0.3560606060606061,0.40464646464646464,0.3642929292929293,0.40545454545454546,0.39631313131313134, 0.3511616161616162]
zero_loss_10 = [0.337, 0.3391111111111111, 0.34055555555555556, 0.3372222222222222,
                0.33766666666666667, 0.33855555555555555, 0.3388888888888889, 0.33644444444444443,
                0.3438333333333333, 0.34144444444444444]
zero_loss_50 = [0.3375, 0.3308, 0.3359, 0.3401, 0.3268, 0.3353, 0.3387, 0.3323, 0.3391,  0.3375]

mean_1 = sum(zero_loss_1)/len(zero_loss_1)
mean_10 = sum(zero_loss_10)/len(zero_loss_10)
mean_50 = sum(zero_loss_50)/len(zero_loss_50)


squared_loss =[]

print(mean_1, mean_10, mean_50)
