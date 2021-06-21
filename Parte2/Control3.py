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

x = np.array([4.4, 4.5, 4.8, 5.5, 5.7, 5.9, 6.3, 6.9, 7.5])
y = np.array([11.3, 9.0, 10.4, 13.8, 12.7, 12.9,
13.8, 16.4, 18.8])

real_y = np.log(y)

X = x.reshape((-1, 1))

model = LinearRegression().fit(X, y)
r_sq = model.score(X, y)
print("Coefficient (r): ", sqrt(r_sq))

a = model.intercept_
b = model.coef_

print("a: ", a)
print("b: ", b)
print("y = {0} e^({1}x)".format(a, b))

#plot_reg(x, y, a, b[0])

#plot_dispersion(x, y)
