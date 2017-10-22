import numpy as np

# part (a)(1)
X1000 = np.array([50,10,37,650,400,80,130])
X10 = np.array([20,30,60,10,100,40])

sum_X1000 = np.sum(X1000)
n1000 = X1000.shape[0]

sum_X10 = np.sum(X10)
n10 = X10.shape[0]

N = 500
alpha = 10
beta = 1

sampled_mu1000 = np.random.gamma(shape=(alpha + sum_X1000), scale=1./(beta + n1000), size=N)
sampled_mu10 = np.random.gamma(shape=(alpha + sum_X10), scale=1./(beta + n10), size=N)

total_1000_ge_10 = np.sum(sampled_mu1000 > sampled_mu10)

print("Q1) a) 1)")
print(np.std(sampled_mu1000))
print(np.std(sampled_mu10))

print(np.std(X1000))
print(np.std(X10))

# print("Empirical probability P[mu_1000 > mu_10 | Data] =", float(total_1000_ge_10)/N)

# part (a)(2)
# look at the variance of the original data
# you have expected and variance

# the vairnce of the simulation should fall between the standard deviation of the original spread!!!!
# see the spread about the poisson and see how it comapres to the original spread

# part (c)
print("Q1 (c)")

normal_X10_sigma_1 = np.random.normal((10*(1**2) + 260) / ((1**2)+6), np.math.sqrt((1**2) / ((1**2) + 6)), size=500)
normal_X1000_sigma_1 = np.random.normal((10*(1**2) + 1357)/((1**2)+7), np.math.sqrt((1**2)/((1**2)+7)), size=500)
total_sigma_1 = np.sum(normal_X1000_sigma_1 > normal_X10_sigma_1)
print(float(total_sigma_1)/N)

normal_X10_sigma_10 = np.random.normal((10*(10**2) + 260)/((10**2)+6), np.math.sqrt((10**2)/((10**2)+6)), size=500)
normal_X1000_sigma_10 = np.random.normal((10*(10**2) + 1357)/((10**2)+7), np.math.sqrt((10**2)/((10**2)+7)), size=500)
total_sigma_10 = np.sum(normal_X1000_sigma_10 > normal_X10_sigma_10)
print(float(total_sigma_10)/N)

normal_X10_sigma_100 = np.random.normal((10*(100**2) + 260)/((100**2)+6), np.math.sqrt((100**2)/((100**2)+6)), size=500)
normal_X1000_sigma_100 = np.random.normal((10*(100**2) + 1357)/((100**2)+7), np.math.sqrt((100**2)/((100**2)+7)), size=500)
total_sigma_100 = np.sum(normal_X1000_sigma_100 > normal_X10_sigma_100)
print(float(total_sigma_100)/N)

