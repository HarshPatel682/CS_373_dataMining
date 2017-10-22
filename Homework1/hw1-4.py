import numpy as np
np.set_printoptions(precision=2)

print("Q4 (a)")

initial_x = np.zeros((100,20), dtype=int)

def create_x(i, j):
    if i <= j:
        return 2*i + j*j + 1
    elif i > j:
        return i*i - 2 * j

def create_y(i):
    return i*i - 1

for i in range(100):
    for j in range(20):
        initial_x[i,j] = create_x(i, j)

initial_y = np.zeros((100,1), dtype=int)

for i in range(100):
    initial_y[i, 0] = create_y(i)

b = np.matmul(np.linalg.inv(np.matmul(initial_x.T, initial_x)), np.matmul(initial_x.T, initial_y))

print(b)

print("Q4 (b)")

value = initial_x[0].dot(b)
print(value)