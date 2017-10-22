import csv
import numpy as np
from matplotlib import use
import math
use('Agg')
import matplotlib.pyplot as plt

ID_for_quill = ""
characterID = []
comicID = []

characterID_num = []
comicID_num = []
file_handler = open("marvel.csv", "r", encoding="utf-8")
reader = csv.reader(file_handler)

dict_whatever = {}
for line in reader:
    characterID.append(line[0])
    comicID.append(line[1])

    characterID_num.append(int(line[0]))
    comicID_num.append(int(line[1]))

    key = int(line[0])
    if dict_whatever.__contains__(key):
        dict_whatever[key].append(int(line[1]))
    else:
        dict_whatever[key] = [int(line[1])]

file_handler.close()

# unique_characterID = []
# # unique_characterID.append(characterID[0])
# k = 0
# for i in characterID:
#     if unique_characterID.__contains__(characterID[k]) is False:
#         unique_characterID.append(characterID[k])
#     k += 1
#
# empty = [""]*len(unique_characterID)
#
# dict_characterID_name = dict(zip(unique_characterID, empty))
#
file_handler = open("marvelCharacters.csv", "r", encoding="utf-8")
reader = csv.reader(file_handler)
for line in reader:
    temp = line[0]
    # dict_characterID_name[temp] = line[1]
    if line[1] == "QUILL":
        ID_for_quill = temp
file_handler.close()

unique_comicID = []
k = 0
for i in comicID:
    if unique_comicID.__contains__(comicID[k]) is False:
        unique_comicID.append(comicID[k])
    k += 1
empty = [""]*len(unique_comicID)
dict_comicID_name = dict(zip(unique_comicID, empty))


file_handler = open("marvelComicBooks.csv", "r", encoding="utf-8")
reader = csv.reader(file_handler)
for line in reader:
    temp = line[0]
    dict_comicID_name[temp] = line[1]
file_handler.close()

# Q3

print("Q3 (a)")

count_appearance = []
total = 0
for i in range(1625):
    if not count_appearance.__contains__(len(dict_whatever[i+1])):
        count_appearance.append(len(dict_whatever[i+1]))
    total += len(dict_whatever[i+1])

count_appearance2 = [0]*len(count_appearance)

dict1 = dict(zip(count_appearance, count_appearance2))
print(count_appearance)

for i in count_appearance:
    key = len(dict_whatever[i])
    dict1[key] += 1

print(dict1)
appearances_after = {}
for i in range(1625):
    key = int(i+1)
    for j in range(1625-i):
        if j > 0:
            appearances_after[key] += len(dict_whatever[j+1])
        else:
            appearances_after[key] = 0

p = 0.8
MAX_DEGREE = 1625
ECCDF = 1.0
x = []
y = []


for d in range(MAX_DEGREE):
    if dict1.__contains__(d+1):
        x.append(dict1[d+1])
        y.append(ECCDF)
        ECCDF = ECCDF - (1-p)*p**d
    else:
        x.append(0)
        y.append(0)

    # ECCDF = ECCDF - (1-p)*p**d
    # y.append(appearances_after[d+1]/total)

plt.xlim([1,max(x)])
plt.xlabel("node degree", fontsize=10)
plt.ylabel("ECCDF", fontsize=10)
plt.loglog(x,y,"ro")
plt.savefig('ECCDF_plot.png')

print("Q3 (b) (i)")

books_quill_is_in = []

k = 0
for i in characterID:
    if characterID[k] == ID_for_quill:
        books_quill_is_in.append(comicID[k])
    k += 1

print("number of books quill is in is: ", len(np.unique(books_quill_is_in)))

print("Q3 (b) (ii)")
empty = [0]*len(unique_comicID)

dict_comicID_character_number = dict(zip(unique_comicID, empty))

k = 0
for i in characterID:
    temp = comicID[k]
    dict_comicID_character_number[temp] += 1
    k += 1

max_id = max(dict_comicID_character_number.values())
num = ""
for keys in dict_comicID_character_number:
    for val in [dict_comicID_character_number[keys]]:
        if val == max_id:
            num = keys

print("comic book with most characters is ", dict_comicID_name[num])

print("Q3 (b) (iii)")

c = max(characterID_num)
d = max(comicID_num)

A = np.zeros( (c + 1 , d + 1) )

k = 0
j = 0
for i in dict_whatever:
    for p in dict_whatever[i]:
        A[i, p] = 1

print("final matrix is ", np.matmul(A, A.T))