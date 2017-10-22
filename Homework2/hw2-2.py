import urllib.request
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

from numpy.linalg import linalg

my_url = "https://www.cs.purdue.edu/homes/ribeirob/courses/Fall2017/data/airpollution.csv"

header_line = True

data = []

local_filename, headers = urllib.request.urlretrieve(my_url)
with open(local_filename) as in_file:
    for line in in_file.readlines():
        if not header_line:
            newLine = line.split(',')
            data.append(newLine[2:8])
        else:
            header_line = False
# print(data)
X = np.array(data, dtype=float)


m_j = []

for i in range(6):
    temp = 1/41 * sum(X[:, i])
    m_j.append(temp)

# print(m_j)

std_hat_j = []

temp = 0
for j in range(6):
    for i in range(41):
        temp += math.pow(X[i, j] - m_j[j], 2)
    temp = math.sqrt(temp * (1/41))
    std_hat_j.append(temp)
    temp = 0

X_prime = np.zeros((41, 6), dtype=float)

for j in range(6):
    for i in range(41):
        X_prime[i, j] = (X[i, j] - m_j[j])/std_hat_j[j]

S = np.zeros((6, 6), dtype=float)

for i in range(41):
    S += 1/41 * np.outer(X_prime[i], np.transpose(X_prime[i]))


# eig_values = linalg.eigvals(S)
eig_values, eig_vectors = linalg.eig(S)

# print(eig_vectors)
for i in range(6):
    eig_values[i] = math.fabs(eig_values[i])

sorted_eig_values = sorted(eig_values, reverse=True)
print("Q2) a)")
for i in range(6):
    print(sorted_eig_values[i])


fig = plt.figure(figsize=(8, 5))

sum_per_column_x_prime = []

for i in range(6):
    temporary = sum(S[:, i])
    sum_per_column_x_prime.append(temporary)


vals = np.arange(len(eig_values))+1
plt.plot(vals, eig_values, 'ro-', linewidth=3)
plt.title("Scree plot")
plt.xlabel("Range")
plt.ylabel("Eig Values")
plt.savefig('ScreePlot.png')
plt.close()

U = np.zeros((6, 2), dtype=float)

for i in range(6):
    U[i, 0] = eig_vectors[i][0]
    U[i, 1] = eig_vectors[i][1]

# print(U)

X_new = np.matmul(X_prime, U)
# print(X_new)
plt.title('Scatter plot for X_new')
plt.scatter(X_new[:, 0], X_new[:, 1])
plt.savefig('ScatterPlotX_new.png')
plt.close()


