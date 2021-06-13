import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt

def plot_dispersion(x, y):
	plt.scatter(x, y)
	plt.show()
	
def plot_reg(x, y, a, b):
	min_x = np.min(x)
	max_x = np.max(x)
	min_y = np.min(y)
	max_y = np.max(y)
	
	x_range = np.linspace(min_x, max_x, 50)
	y_range = np.zeros(50)
	for i in range(50):
		y_range[i] = a + b*x_range[i]
	
	plt.scatter(x, y)
	plt.plot(x_range, y_range, c='orange')
	plt.show()

# Problema ejemplo 1	

x = np.arange(0, 4, 0.2)
y = np.array([5.06, 5.01, 5.12, 5.13, 5.14, 5.16, 5.25, 5.19, 5.24, 5.46, 5.40, 5.57, 5.47, 5.53, 5.61, 5.59, 5.61, 5.75, 5.68, 5.80])

X = x.reshape((-1, 1))

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("y = {0} + {1}x".format(a, b))

#plot_reg(x, y, a, b[0])

#plot_dispersion(x, y)

# Problema cuestionario

x = np.array([27, 45, 72, 58, 31, 60, 34, 74])
y = np.array([250, 285, 310, 295, 265, 298, 267, 320])

print("----------------")
X = x.reshape((-1, 1))

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("R2: ", r_sq)
print("Coefficient (r): ", sqrt(r_sq))

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("y = {0} + {1}x".format(a, b))

