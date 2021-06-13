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

y = np.array([169.0, 218.5, 216.5, 225.0, 229.9,
235.0, 239.9, 247.9, 260.0, 269.9, 234.9, 255.0,
269.9, 294.5, 309.9])

x1 = np.array([6, 10, 10, 11, 13, 13, 13, 17, 19,
18, 13, 18, 17, 20, 21])

x2 = np.array([1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1,
2, 2, 2])

x3 = np.array([2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4,
4, 4, 4])

x4 = np.array([1, 2, 2, 2, 1.7, 2.5, 2, 2.5, 2, 2, 2, 2, 3, 3, 3])

print(len(y), len(x1), len(x2), len(x3), len(x4))

#X = x.reshape((-1, 1))

X = np.array([x1, x2, x3, x4])
print(X)
X = X.transpose()
print(X)

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

#fvalue, pvalue = stats.f_oneway(y, x1, x2, x3, x4)
#print(fvalue, pvalue)
