import csv
import numpy as np

from collections import defaultdict
import urllib
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

# opening the file, then reading it later on
file_handler = open("retail.csv", "r", encoding="utf-8")
reader = csv.reader(file_handler)

header_line = True

# list of each parameter
invoiceNo = []
stockCode = []
description = []
quantity = []
invoiceDate = []
unitPrice = []
customerID = []
country = []

everything = []
head = []
# stores all of the info in respective lists
for line in reader:
    if not header_line:
        invoiceNo.append(line[0])
        stockCode.append(line[1])
        description.append(line[2])
        quantity.append(line[3])
        invoiceDate.append(line[4])
        unitPrice.append(line[5])
        customerID.append(line[6])
        country.append(line[7])
        everything.append(line)
    else:
        header_line = False
        head = line

file_handler.close()


# NUMBER 1

# prints out the length (not including the header line)
# number 1 (a)
print("Q2 number 1 item (a)")
print("number of items is: ", len(invoiceNo))

# uses numpy to get a list of all unique ids
# number 1 (b)
print("Q2 number 1 item (b)")
num_unique_ids = np.unique(stockCode)
print("number of unique stock codes is: ", len(num_unique_ids))

# NUMBER 2

# number 2 (a)
print("Q2 number 2 item (a)")
count = stockCode.count("20685")
total_unit = 0
k = 0
for i in stockCode:
    if stockCode[k] == "20685":
        total_unit += float(unitPrice[k])
    k += 1

average_unit_price = total_unit/count
print("Unit price is: ", average_unit_price)

# number 2 (b)
print("Q2 number 2 item (b)")
hours = []
l = [i.split(' ',1)[1] for i in invoiceDate]
l2 = [i.split(':',1)[0] for i in l]

j = 0
for i in l2:
    if len(hours) == 0:
        hours.append(l2[j])
    else:
        if hours.__contains__(l2[j]) is False:
            hours.append(l2[j])
    j += 1

l3 = []
for i in hours:
    l3.append(0)


key_value = dict(zip(hours, l3))

k = 0
for i in invoiceDate:
    temp = l2[k]
    key_value[temp] += int(quantity[k])
    k += 1

# print(key_value)

maximum = 0
k = 0
highest_hour = 0
for i in key_value:
    temp1 = key_value[hours[k]]
    if int(maximum) < int(temp1):
        maximum = temp1
        highest_hour = hours[k]
    k += 1

print("the highest paying hour is: ", highest_hour)

# number 2 (c)
print("Q2 number 2 item (c)")
name_of_countries = []
k = 0
for i in country:
    if len(name_of_countries) == 0:
        name_of_countries.append(country[k])
    else:
        if name_of_countries.__contains__(country[k]) is False:
            name_of_countries.append(country[k])
    k += 1

l4 = [0]*len(name_of_countries)
country_spent = dict(zip(name_of_countries, l4))

k = 0
for i in country:
    temp = country[k]
    temp_num = float(quantity[k])
    temp_num1 = float(unitPrice[k])
    temp_num2 = temp_num * temp_num1
    country_spent[temp] += temp_num2
    k += 1

spent_correct_amount = []
k = 0
for i in name_of_countries:
    if country_spent[name_of_countries[k]] > 50000:
        spent_correct_amount.append(name_of_countries[k])
    k += 1

# print(country_spent)

# x axis for plot
# print(spent_correct_amount)

l5 = [0]*len(spent_correct_amount)

bar = dict(zip(spent_correct_amount, l5))

k = 0
for i in spent_correct_amount:
    temp = spent_correct_amount[k]
    bar[temp] += float(country_spent[spent_correct_amount[k]])
    k += 1
print(bar)
print("Graph was made in bar1.png")

# y axis
y_axis = [0]*len(spent_correct_amount)
k = 0
for i in spent_correct_amount:
    temp = spent_correct_amount[k]
    y_axis[k] += bar[temp]
    k += 1

ind = np.arange(len(spent_correct_amount))
plt.bar(ind, y_axis)
plt.xticks(ind + .05, spent_correct_amount)
plt.savefig('bar1.png')

# number 3
print("Q2 number 3")

np.random.shuffle(everything)
half = len(invoiceDate)/2

with open("output-1.csv", "w") as file:
    file_writer = csv.writer(file)
    k = 0
    file_writer.writerow(head)
    while k < half:
        file_writer.writerow(everything[k])
        k += 1
file.close()

with open("output-2.csv", "w") as file1:
    file_writer1 = csv.writer(file1)
    file_writer1.writerow(head)
    while k < len(invoiceDate):
        file_writer1.writerow(everything[k])
        k += 1
file1.close()
