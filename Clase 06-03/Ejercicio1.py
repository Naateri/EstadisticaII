import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from math import sqrt
import scipy

# Importando data

data = pd.read_excel('23 - Old Faithful.xlsx', 
	engine='openpyxl')
	
# Modelo regresion lineal de INTERVALO POSTERIOR a partir de DURACION, ALTURA e INTERVALO ANTERIOR.

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

y = np.array(data["INTERVALO ANTERIOR"])[:-1]

x1 = np.array(data["DURACION"])[:-1]

x2 = np.array(data["ALTURA"])[:-1]

x3 = np.array(data["INTERVALO ANTERIOR"])[:-1]

print(len(y), len(x1), len(x2), len(x3))

print(y)

#X = x.reshape((-1, 1))

X = np.array([x1, x2, x3])
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
